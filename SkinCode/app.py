from flask import Flask, render_template, request, redirect, url_for, session
import pyotp
import qrcode
import io
import base64
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Segurança da sessão

# Gera o segredo base para o Google Authenticator
TOTP_SECRET = pyotp.random_base32()

@app.route('/')
def index():
    if 'authenticated' in session and session['authenticated']:
        return render_template('index.html', authenticated=True)
    else:
        return redirect(url_for('auth'))

@app.route('/auth', methods=['GET', 'POST'])
def auth():
    totp = pyotp.TOTP(TOTP_SECRET)
    otp_uri = totp.provisioning_uri(name="SkinCodeUser", issuer_name="SkinCode")

    # Gerar QR Code
    qr = qrcode.make(otp_uri)
    buffered = io.BytesIO()
    qr.save(buffered, format="PNG")
    qr_code = base64.b64encode(buffered.getvalue()).decode("utf-8")

    if request.method == 'POST':
        code = request.form.get('code')
        if totp.verify(code):
            session['authenticated'] = True
            return redirect(url_for('index'))
        else:
            return render_template('auth.html', error="Código inválido", qr_code=qr_code)

    return render_template('auth.html', qr_code=qr_code)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth'))

if __name__ == '__main__':
    app.run(debug=True)


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Hospital Data Analytics",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Função para gerar dados simulados realistas
@st.cache_data
def generate_hospital_data():
    """Gera dados simulados baseados em experiência real de UTI/Emergência"""
    
    # Dados de 90 dias
    dates = pd.date_range(start='2024-01-01', end='2024-03-31', freq='D')
    
    # Simulando dados realistas de UTI/Emergência
    np.random.seed(42)
    
    data = []
    for date in dates:
        # Variação semanal (fins de semana têm menos internações eletivas)
        weekday_factor = 0.8 if date.weekday() >= 5 else 1.0
        
        # Dados diários
        daily_data = {
            'date': date,
            'total_patients': np.random.poisson(45) * weekday_factor,
            'icu_patients': np.random.poisson(12),
            'emergency_patients': np.random.poisson(85) * weekday_factor,
            'surgery_patients': np.random.poisson(8) * weekday_factor,
            'discharge_patients': np.random.poisson(35),
            'mortality_rate': np.random.uniform(0.02, 0.08),
            'avg_length_stay': np.random.uniform(3.5, 7.2),
            'bed_occupancy': np.random.uniform(0.75, 0.95),
            'staff_ratio': np.random.uniform(1.2, 2.8),  # Enfermeiros por paciente
            'readmission_rate': np.random.uniform(0.05, 0.15)
        }
        data.append(daily_data)
    
    return pd.DataFrame(data)

# Função para criar gráfico de tendências
def create_trend_chart(df):
    """Cria gráfico de tendências principais"""
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Pacientes por Dia', 'Taxa de Ocupação', 
                       'Tempo Médio de Internação', 'Taxa de Mortalidade'),
        specs=[[{"secondary_y": False}, {"secondary_y": False}],
               [{"secondary_y": False}, {"secondary_y": False}]]
    )
    
    # Pacientes por dia
    fig.add_trace(
        go.Scatter(x=df['date'], y=df['total_patients'], 
                  name='Total Pacientes', line=dict(color='blue')),
        row=1, col=1
    )
    
    # Taxa de ocupação
    fig.add_trace(
        go.Scatter(x=df['date'], y=df['bed_occupancy']*100, 
                  name='Ocupação (%)', line=dict(color='red')),
        row=1, col=2
    )
    
    # Tempo médio de internação
    fig.add_trace(
        go.Scatter(x=df['date'], y=df['avg_length_stay'], 
                  name='Dias Médios', line=dict(color='green')),
        row=2, col=1
    )
    
    # Taxa de mortalidade
    fig.add_trace(
        go.Scatter(x=df['date'], y=df['mortality_rate']*100, 
                  name='Mortalidade (%)', line=dict(color='orange')),
        row=2, col=2
    )
    
    fig.update_layout(height=600, showlegend=False, 
                     title_text="Análise de Tendências Hospitalares")
    return fig

# Função para análise de correlação
def create_correlation_heatmap(df):
    """Cria mapa de calor de correlações"""
    correlation_cols = ['total_patients', 'icu_patients', 'emergency_patients',
                       'mortality_rate', 'avg_length_stay', 'bed_occupancy', 
                       'staff_ratio', 'readmission_rate']
    
    corr_matrix = df[correlation_cols].corr()
    
    fig = px.imshow(corr_matrix, 
                    text_auto=True, 
                    aspect="auto",
                    title="Correlação entre Métricas Hospitalares")
    return fig

# Função para indicadores KPI
def display_kpis(df):
    """Exibe KPIs principais"""
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        avg_patients = df['total_patients'].mean()
        st.metric("Média Pacientes/Dia", f"{avg_patients:.1f}")
    
    with col2:
        avg_occupancy = df['bed_occupancy'].mean() * 100
        st.metric("Taxa Ocupação Média", f"{avg_occupancy:.1f}%")
    
    with col3:
        avg_mortality = df['mortality_rate'].mean() * 100
        st.metric("Taxa Mortalidade", f"{avg_mortality:.2f}%")
    
    with col4:
        avg_stay = df['avg_length_stay'].mean()
        st.metric("Tempo Médio Internação", f"{avg_stay:.1f} dias")

# Interface principal
def main():
    st.title("🏥 Hospital Data Analytics Dashboard")
    st.markdown("*Desenvolvido por José Roberto Breccio - Enfermeiro + Desenvolvedor Python*")
    st.markdown("---")
    
    # Sidebar para filtros
    st.sidebar.header("Filtros de Análise")
    
    # Carregamento dos dados
    df = generate_hospital_data()
    
    # Filtro de data
    date_range = st.sidebar.date_input(
        "Selecione o período:",
        value=(df['date'].min(), df['date'].max()),
        min_value=df['date'].min(),
        max_value=df['date'].max()
    )
    
    # Filtrar dados
    if len(date_range) == 2:
        mask = (df['date'] >= pd.Timestamp(date_range[0])) & (df['date'] <= pd.Timestamp(date_range[1]))
        df_filtered = df[mask]
    else:
        df_filtered = df
    
    # Exibir KPIs
    st.header("📊 Indicadores Principais")
    display_kpis(df_filtered)
    
    # Gráfico de tendências
    st.header("📈 Análise de Tendências")
    trend_fig = create_trend_chart(df_filtered)
    st.plotly_chart(trend_fig, use_container_width=True)
    
    # Análise de correlação
    st.header("🔍 Análise de Correlação")
    corr_fig = create_correlation_heatmap(df_filtered)
    st.plotly_chart(corr_fig, use_container_width=True)
    
    # Insights baseados na experiência
    st.header("💡 Insights Clínicos")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Análise UTI")
        icu_avg = df_filtered['icu_patients'].mean()
        st.write(f"**Média UTI:** {icu_avg:.1f} pacientes/dia")
        
        if df_filtered['staff_ratio'].mean() < 1.5:
            st.warning("⚠️ Ratio enfermeiro/paciente abaixo do ideal")
        else:
            st.success("✅ Ratio enfermeiro/paciente adequado")
    
    with col2:
        st.subheader("Análise Emergência")
        emergency_avg = df_filtered['emergency_patients'].mean()
        st.write(f"**Média Emergência:** {emergency_avg:.1f} pacientes/dia")
        
        if df_filtered['readmission_rate'].mean() > 0.10:
            st.warning("⚠️ Taxa de readmissão elevada")
        else:
            st.success("✅ Taxa de readmissão controlada")
    
    # Dados detalhados
    st.header("📋 Dados Detalhados")
    if st.checkbox("Mostrar dados brutos"):
        st.dataframe(df_filtered)
    
    # Exportar dados
    st.header("💾 Exportar Dados")
    if st.button("Gerar Relatório CSV"):
        csv = df_filtered.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name=f"hospital_analytics_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )

if __name__ == "__main__":
    main()


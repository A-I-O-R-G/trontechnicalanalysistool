# 📝 Documentação do Projeto: Análise Técnica da Criptomoeda Tron (TRX)

## 📖 Introdução
Este projeto visa a criação de um script para realizar a análise técnica da criptomoeda Tron (TRX). O objetivo principal é coletar, analisar e visualizar dados de preços históricos e volumes de negociação, proporcionando insights para traders e investidores.

### Funcionalidades-chave:
- Coleta de dados históricos de preços e volumes de negociação da Tron.
- Cálculo de diversos indicadores técnicos, como médias móveis, RSI, e MACD.
- Visualização dos dados em gráficos interativos.

---

## ⚙️ Instalação

### Requisitos do Sistema:
- Python 3.x.
- Bibliotecas necessárias: 
  - `requests`
  - `pandas`
  - `numpy`
  - `plotly`
  
### Dependências Necessárias:
```bash
pip install requests pandas numpy plotly
```

### Guia Passo-a-Passo:
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu_usuario/analisetecnica_tron.git
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd analisetecnica_tron
   ```
3. Instale as dependências conforme indicado acima.

### Configuração Inicial:
- Nenhuma configuração adicional é necessária para iniciar o projeto.

---

## 🔍 Uso

### Exemplos Práticos:
Execute o script principal para coletar dados e gerar gráficos:
```bash
python main.py
```

### Comandos Principais:
- **`coletar_dados_historicos(symbol, interval='1d', limit=100)`**: Coleta dados históricos da Tron usando a API da Binance.
- **`media_movel(df, period)`**: Calcula a média móvel dos preços.
- **`calcular_rsi(df, period=14)`**: Calcula o Índice de Força Relativa (RSI).
- **`plotar_graficos(df)`**: Gera gráficos interativos com os dados coletados.

### Configurações Disponíveis:
- `symbol`: Par de negociação (ex: 'TRXUSDT').
- `interval`: Intervalo para a coleta de dados (opcional, padrão é '1d').

### Casos de Uso Comuns:
- Análise diária dos preços da Tron.
- Identificação de padrões de comportamento de mercado.

---

## 📁 Estrutura do Projeto
```
analisetecnica_tron/
├── main.py             # Script principal para análise técnica
├── requirements.txt    # Dependências do projeto
└── README.md           # Documentação deste projeto
```

---

## 🌐 API

### Endpoints Disponíveis:
- `GET https://api.binance.com/api/v3/klines`: Coleta dados de preços históricos para a Tron.

### Métodos e Parâmetros:
- **Método**: `GET`
- **Parâmetros**:
  - `symbol`: O par de negociação, ex: 'TRXUSDT'.
  - `interval`: O intervalo para as velas, ex: '1d'.
  - `limit`: Limite de dados a serem coletados.

### Exemplos de Requisições:
```python
coletar_dados_historicos('TRXUSDT')
```

### Respostas Esperadas:
```json
[
    ["open_time", "open", "high", "low", "close", "volume", ...]
]
```

---

## 🤝 Contribuição

### Guia para Contribuidores:
1. Crie um fork do repositório.
2. Crie sua branch:
   ```bash
   git checkout -b feature/nome-da-sua-feature
   ```
3. Faça alterações e commit:
   ```bash
   git commit -m 'Adiciona nova funcionalidade'
   ```
4. Envie para o repositório remoto:
   ```bash
   git push origin feature/nome-da-sua-feature
   ```

### Padrões de Código:
- Utilize PEP 8 para a formatação Python.

### Processo de Pull Request:
- Abra um pull request na interface do GitHub descrevendo suas alterações.

### Boas Práticas:
- Documente suas funções e métodos.
- Teste suas alterações antes de enviar.

---

## 📜 Licença

### Tipo de Licença:
Este projeto está licenciado sob a Licença MIT.

### Termos de Uso:
Liberdade para uso, cópia, modificação e distribuição do software.

### Restrições:
Inclua o aviso de licença em qualquer distribuição do software.

---

## 🛠️ Manutenção Contínua
Mantemos atualizações regulares e melhorias contínuas no script, visando sempre a precisão e a eficiência do código.

---

## 🔄 Atualizações Recentes
### Status do Desenvolvimento:
O projeto tem evoluído, incorporando mudanças significativas:
- Refatoração das funções para melhorar a modularidade e legibilidade.
- Adição de tratamento de erros para requisições à API.
- Inclusão de tipagem nas funções para maior clareza.
- Melhoria na documentação do código.

---

Esta documentação foi estruturada para fornecer informações claras e completas sobre a implementação e utilização do software. Se houver mais detalhes que você gostaria de incluir ou ajustar, não hesite em avisar!
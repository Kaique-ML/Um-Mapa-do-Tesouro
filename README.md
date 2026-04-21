O objetivo aqui é mostrar a "linha lógica clara" exigida no enunciado. Substitua o conteúdo do seu arquivo README.md por este modelo estruturado:

# 📑 Um-Mapa-do-Tesouro: Gestão de Eficiência na Colheita de Cana

Sistema desenvolvido para monitoramento de produtividade e redução de perdas na colheita mecanizada de cana-de-açúcar, focado nos desafios do agronegócio brasileiro.

## 🎯 O Problema (A Dor do Negócio)
Conforme dados da SOCICANA, a colheita mecanizada de cana pode gerar perdas de até 15%, resultando em prejuízos anuais de R$ 20 milhões apenas no estado de São Paulo. Nosso sistema atua como uma Agrotech para identificar essas perdas e otimizar o TCH (Toneladas de Cana por Hectare).

## 🚀 Funcionalidades Implementadas

**Cadastro de Produtores**: Registro com geolocalização e persistência em Banco de Dados Oracle.

**Gestão de Lavouras**: Controle de área plantada e cultura específica.

**Análise de Perdas**: Algoritmo que identifica desperdícios acima do limite esperado (15% mecanizada / 5% manual).

**Cálculo de TCH**: Monitoramento real da produtividade por hectare.

**Persistência Híbrida**: Dados salvos localmente em JSON e remotamente em Oracle SQL.

## 📂 Estrutura do Projeto

**main.py**: Ponto de entrada e menu do sistema.

**cadastro.py**: Lógica de formulários e integração com banco.

**analise_producao.py**: Subalgoritmos de cálculos matemáticos e alertas.

**banco_oracle.py**: Configurações de conexão e comandos SQL.

**arquivos.py**: Manipulação de leitura e escrita de arquivos JSON.

## ⚙️ Como Executar

Certifique-se de ter o Python 3.10+ instalado.

Instale a biblioteca do banco: 'pip install oracledb'.

Configure suas credenciais no arquivo 'banco_oracle.py'.

Execute o comando: 'python src/main.py'.

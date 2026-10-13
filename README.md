# MDI - Curitiba: Memorial Descritivo Inteligente
[![QGIS](https://img.shields.io/badge/QGIS-3.44%2B-589632?logo=qgis&logoColor=white)](https://qgis.org)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)
[![Plugin Version](https://img.shields.io/badge/version-0.2.0-blue)](#)
[![Status](https://img.shields.io/badge/status-em_desenvolvimento-orange)](#)
[![License](https://img.shields.io/badge/license-GPLv3-blueviolet.svg)](https://www.gnu.org/licenses/gpl-3.0)

## Introdução

Este é um Plugin QGIS desenvolvido para automatizar a redação de memoriais descritivos de parcelamento de solo, seguindo padrões utilizados por algumas entidades em Curitiba - PR.

O  programa gera um arquivo final contendo o memorial descritivo redigido a partir de arquivos shapefile com camadas vetoriais representando cada lote. Os dados de geometria, como área, medidas, e confrontações, são extraídos automaticamente. Os demais dados, como nomes e códigos de plantas, lotes, arquitetos, são informados pelo usuário. O texto final é composto no padrão indicado, e pode ser salvo em um arquivo .docx a partir de um arquivo template fornecido pelo usuário.

O processo é simples e personalizado para tarefas específicas, atendendo às necessidades reais de uma determinada entidade. O objetivo é facilitar a redação de memoriais, a partir da coleta automática de dados.

## Pré-Requisitos

- QGIS em versão 3.44 ou superior.
    
Não é necessário instalar nenhuma outra biblioteca, já que a dependência python-docx está sendo distribuída juntamente com o plugin. Essa biblioteca foi adaptada de forma a reutilizar as subdependências que já estão inclusas do próprio QGIS.

## Instalação

No momento há duas opções disponíveis para instalação: a partir do arquivo .zip, ou a partir do link de repositório. A instalação a partir do link de repositório possibilita receber avisos de atualizações, e facilita a atualização automática, por isso é preferível.

### Instalar no QGIS a partir do arquivo .zip

#### Passo 1: Baixar o Plugin
1. Vá até a seção [**Releases**](https://github.com/eduardo-c-siqueira/cria-memorial-qgis/releases) do repositório (no lado direito da [página principal](https://github.com/eduardo-c-siqueira/cria-memorial-qgis) do GitHub).
2. Clique no lançamento mais recente e, na seção **Assets**, clique no arquivo `mdi_curitiba.zip` para baixá-lo.

   > **Atenção:** Não descompacte (não extraia) o arquivo `.zip`. O QGIS precisa do arquivo compactado.


#### Passo 2: Instalar no QGIS
1. Abra o **QGIS**.
2. No menu superior, acesse **Complementos** > **Gerenciar e Instalar Complementos...**
3. No menu lateral esquerdo da janela que abrir, clique em **Instalar a partir do ZIP**.
4. No campo **Arquivo ZIP**, clique no botão com três pontos (`...`) e selecione o arquivo `.zip` que você baixou.
5. Clique no botão **Instalar complemento**.

*Como verificar se funcionou:* Se a instalação for concluída com sucesso, uma barra amarela aparecerá no topo do QGIS com a mensagem *"Complemento instalado com sucesso"*, e o ícone do plugin ficará visível na sua barra de ferramentas ou no menu *Complementos*.

### Instalar no QGIS a partir de um link de repositório

1. No menu superior do QGIS, acesse **Complementos** > **Gerenciar e Instalar Complementos...**

2. No menu lateral esquerdo da janela que abrir, clique em **Opções**.

3. Clique no botão **Adicionar...** em "Repositórios de Complementos", logo abaixo da lista de repositórios.

4. Defina um nome e cole a URL *https://github.com/eduardo-c-siqueira/cria-memorial-qgis/plugins.xml*.

O plugin passará a aparecer na aba **Não Instalados** ou **Tudo** do gerenciador do QGIS.

## Como usar
	
Antes de iniciar, é recomendado que o usuário já tenha um arquivo .docx de template preparado salvo na máquina. Recomenda-se que seja um arquivo vazio, com o cabeçalho pronto de acordo com o padrão institucional próprio.

Depois de instalado, o plugin pode ser acionado a partir da opção “Complementos” na barra superior do QGIS, ou por meio do ícone na Barra de Ferramentas, se a exibição de Complementos estiver ativada.

### Passo a passo:
	
1. Selecione as features que farão parte do documento final (_inclusive as representações de lotes confrontantes_), utilizando a ferramenta de seleção do QGIS

2. Acione o plugin

3. Preencha as informações gerais e escolha o tipo de memorial na primeira janela

4. Preencha as informações requeridas nas próximas janelas. Estas etapas variam de acordo com o tipo de memorial escolhido

5. Na janela final, de exibição do texto elaborado, você pode clicar em **Configurações** para escolher o tipo de saída e indicar os arquivos de template/logos que serão utilizados para a saída final _(a configuração padrão de saíde é .docx)_

6. Ao final, escolha um nome para o arquivo e o local onde será salvo.

### Entradas e saídas geradas

#### Entradas:
- Shapefiles:
     - Devem conter features de polígono ou multipolígono, representando cada lote participante do processo (incluindo lotes confrontantes)

- Template docx ou logos:

    - Para template .docx é recomendado um documento preparado para receber o texto final (com cabeçalho pronto e corpo vazio).

    - Para a alternativa de PDF uma logo nas proporções 80x80 como logo da prefeitura, e uma logo de proporção 140x50 (altura x largura) como logo da autarquia.

#### Saídas:
- Docx ou PDF, dependendo da escolha do usuário, com o texto montado a partir dos dados fornecidos.

>OBS.: A opção de saída em PDF foi criada como plano B, para o caso de algum componente falhar na funcionalidade docx. Recomenda-se utilizar preferencialmente a opção de docx como saída, devido à flexibilidade e maior controle do usuário sobre o resultado final.


### Próximos passos (Roadmap)

Para as próximas versões do plugin, pretendo fazer melhorias em relação a otimização e padronização do código, ajustes na aparência e apresentação da interface de usuário, funcionalidades acessórias, e desenvolvimento do fluxo de outros tipos de memorial

#### Melhorias de código
	
- Reorganição do código seguindo padrões de arquitetura que facilitem a manutenção e entendimento do código
- Preparação do código para a implementação dos outros tipos de memorial

#### Interface de usuário

- Ajustes de títulos e fraseamento das etapas
- Ajustes de tamanhos e posição das janelas
- Simplificação da seleção de lados nos memoriais “padrão”
- Possibilidade do usuário selecionar as features a serem usadas depois de já iniciado o processo.

#### Funcionalidades acessórias

- Menu de ajuste de configurações antes do início do fluxo
- Memória: Rua x Código, Planta x Código e Arquiteto x CAU
- Salvamento e carregamento de memoriais finalizados ou não.
- Possibilidade de edição do texto na etapa final
- Ajustes na formatação final do texto em .docx.
- Possibilidade de “memorial encravado” (ou seja, vários memoriais em um único arquivo .docx)

#### Outros tipos de memorial

- Memorial de Subdivisão de lote
- Memorial de Unificação de lotes
- Memorial de Subdivisão e Unificação de lotes
- Memorial Transitório (subdivisão provisória)


## Contribuições

Você pode contribuir com o plugin **MDI - Curitiba** ao sugerir melhorias ou reportar problemas utilizando a aba de **Issues** do repositório.

### Como abrir uma Issue:

1. Acesse a aba [Issues](https://github.com/eduardo-c-siqueira/cria-memorial-qgis/issues) do repositório e clique em **New Issue**.
2. Escolha o modelo apropriado para o seu caso:
   - **Relato de Bug:** Para falhas, comportamentos inesperados ou erros de execução do Python no QGIS.
   - **Sugestão de Melhoria:** Para sugerir novas funcionalidades ou aprimoramentos de ferramentas.
3. Preencha os campos solicitados:
   - **Requisitos de ambiente:** Lembre-se de confirmar se você está utilizando o **QGIS 3.44 ou superior**.
   - **Log de Erros:** Sempre que possível, inclua o log de erro do Python do QGIS (disponível em `Exibir` > `Painéis` > `Registro de mensagens` > aba *Erros Python* ou *Complementos*).
4. Antes de enviar, verifique se o problema já não foi relatado por outro usuário utilizando o campo de busca.



## Licença

Este projeto está licenciado sob os termos da **GNU General Public License v3.0 (GPL-3.0)**. 

Você é livre para usar, estudar, modificar e redistribuir este software sob as condições da licença GPLv3. Para mais detalhes, consulte o arquivo [LICENSE](./LICENSE) presente na raiz deste repositório.

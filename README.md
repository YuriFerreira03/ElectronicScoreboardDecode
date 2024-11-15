# Decodificação do Controlador de Placar Eletrônico PC5-B

Este projeto visa decodificar o controlador do placar eletrônico **Tecnodis PC5-B** para permitir que ele seja controlado por um aplicativo móvel, substituindo o controle manual por um sistema digital. Utilizando Python e técnicas de engenharia reversa, é possível captar e interpretar os sinais enviados pelo controlador, permitindo que os comandos sejam enviados de forma programática.

## Descrição do Projeto

O controlador **PC5-B**, comumente utilizado em ginásios para ajustar pontuações e cronômetros, possui uma série de botões físicos. A decodificação desses sinais possibilita controlar o placar remotamente através de um aplicativo.

## Principais Componentes Utilizados

- **Controlador PC5-B** da Tecnodis: controlador físico de placar eletrônico.
- **Adaptador USB-TTL**: utilizado para converter sinais entre o controlador e o sistema digital.
- **Circuito Integrado SN74LS**: componente essencial para a interface de sinais, permitindo a leitura consistente dos comandos.
- **Breadboard e Jumpers**: usados para conectar o circuito e realizar prototipagem.
- **Python**: linguagem de programação usada para decodificar e interpretar os sinais capturados.
- **VS Code**: ambiente de desenvolvimento utilizado para execução do código.

---


# 🌟 Automação de Envio de Mensagens e Imagens pelo WhatsApp 📱

Este projeto utiliza a biblioteca `pywhatkit` para enviar mensagens de texto 💬 e imagens 📸 automaticamente via WhatsApp. A aplicação permite que você envie mensagens de boas-vindas 🎉 e imagens personalizadas para uma lista de contatos de forma agendada ⏰ e com um pequeno atraso configurável.

## 🚀 Funcionalidades

- 💌 Enviar mensagens de texto via WhatsApp.
- 🖼️ Enviar imagens com legenda via WhatsApp.
- 📲 Enviar mensagens e imagens para múltiplos contatos em sequência.
- 📝 Log de eventos e erros em um arquivo `whatsapp_log.txt`.

## 🛠️ Pré-requisitos

Antes de usar este script, você precisa instalar as seguintes bibliotecas:

1. 📦 `pywhatkit`: Para enviar mensagens e imagens via WhatsApp.
2. ⏳ `time`: Para controle de tempo e atraso no envio.
3. 🖊️ `logging`: Para registrar logs de eventos e erros.

Você pode instalar o `pywhatkit` utilizando o pip:

```bash
pip install pywhatkit
```

## 📋 Como Usar

1. 🖥️ Clone este repositório em sua máquina:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

2. 📁 Navegue até a pasta do projeto:

```bash
cd nome-do-repositorio
```

3. 🛠️ Edite o script para adicionar os números de telefone 📞 (no formato `+55` para Brasil) e a mensagem/imagem que deseja enviar.

4. ▶️ Execute o script:

```bash
python script.py
```

## 💡 Exemplo de Uso

Aqui está um exemplo de como enviar uma mensagem e uma imagem para uma lista de contatos:

```python
if __name__ == "__main__":
    # Lista de números de telefone (com código do país +55 para Brasil)
    numeros = ["+5518XXXXXXXX", "+5518XXXXXXXX"]

    # Caminho da imagem que você deseja enviar
    imagem = r"C:\Users\Andre Junior\Downloads\Nova pasta\amor.jpg"

    # Mensagem de boas-vindas
    mensagem = "Olá! Seja bem-vindo à Loja Online"

    # Enviar mensagem e imagem para todos os números da lista
    enviar_para_contatos(numeros, imagem, mensagem)
```

## 📄 Logs

Todos os eventos e erros são registrados no arquivo `whatsapp_log.txt`, permitindo que você rastreie o status do envio de mensagens.

## ⚠️ Observações

- 🌐 O WhatsApp Web precisa estar conectado no navegador para que as mensagens sejam enviadas.
- ✅ Certifique-se de que o caminho da imagem está correto e que você tem as permissões necessárias para acessar o arquivo.

## 🤝 Contribuindo

Sinta-se à vontade para enviar PRs ou sugerir melhorias! Todo feedback é bem-vindo 💡.

## 📜 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

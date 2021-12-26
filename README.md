# Engana-Firewall
License: None; Public Domain.
Developed by DEK.

(en-US)
Developed in Python, this tool is specially designed to make Web requests with a Python file, going over firewalls that check if the user is using the browser. To use it, just pass a URL, the User-Agent and the Cookie. These can be obtained from the browser console (F12, Ctrl+Shift+i, Ctrl+Shift+C or Ctrl+Shift+J).
In the case of Mozilla Firefox, we simply access the Network and Storage tabs, respectively; copy the contents of the section and paste it into the referring fields during code execution.
This will bring us the content of the page in HTML. If you want to bring it into normal content, just remove the .read() method from the html variable on line 19.

(pt-BR)
Desenvolvida em Python, esta ferramenta foi especialmente pensada para fazer requisições Web com um arquivo em Python, passando por cima dos Firewalls que verificam se o usuário está utilizando o navegador. Para utilizá-la, basta passarmos uma URL, o User-Agent e o Cookie. Estes podem ser obtidos no console do navegador (F12, Ctrl+Shift+i, Ctrl+Shift+C ou Ctrl+Shift+J).
No caso do Mozilla Firefox, basta acessarmos as abas Network e Storage, respectivamente; copiarmos o conteúdo da seção e colarmos nos campos referentes durante a execução do código.
Este nos trará o conteúdo da página em HTML. Se desejar trazê-lo em conteúdo normal, basta retirarmos o método .read() da variável html, na linha 19.

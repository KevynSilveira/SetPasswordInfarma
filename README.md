Sistema de Alteração de Senha Logística - README
Este é um sistema de interface gráfica desenvolvido em Python que permite aos usuários alterar suas senhas para um padrão específico usado no contexto logístico. O sistema utiliza a biblioteca customtkinter para criar a interface gráfica e interage com um banco de dados SQL Server através da biblioteca pyodbc.

Funcionalidades

Interface Gráfica Amigável: O sistema oferece uma interface gráfica intuitiva que facilita a interação do usuário.
Acesso ao Banco de Dados: O sistema se conecta a um banco de dados SQL Server para realizar operações de atualização.
Alteração de Senha: Os usuários podem inserir um código de login e a senha associada a esse código será alterada para um padrão predefinido.
Feedback Visual: O sistema exibe mensagens de sucesso ou erro através de caixas de diálogo.
Modo de Aparência Personalizável: A interface gráfica permite a escolha entre os modos de aparência claro e escuro.

Requisitos
Python 3.x
Bibliotecas: customtkinter, pyodbc

Execução

Instale as bibliotecas necessárias executando pip install customtkinter pyodbc no terminal.
Clone ou baixe este repositório para o seu computador.
Abra um terminal e navegue até o diretório onde o código está localizado.
Execute o arquivo main.py usando o Python: python main.py.
A interface gráfica será exibida.
Insira o código de login e clique no botão "Executar".
A senha associada ao código de login será alterada para um padrão.

Observações

Certifique-se de configurar corretamente as credenciais do banco de dados na função access_db().
Este sistema é um exemplo educativo e pode ser adaptado para uso em ambientes de produção, levando em consideração questões de segurança.
Para dúvidas ou problemas, entre em contato em kevynsilveira0610@gmail.com.
Aviso: Este sistema é fornecido apenas como exemplo e não leva em consideração todas as práticas recomendadas de segurança. Certifique-se de proteger adequadamente o acesso ao banco de dados e informações sensíveis.

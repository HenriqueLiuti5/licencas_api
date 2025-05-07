🔐 Licenças API – Sistema de Controle de Licenças
API desenvolvida em Python com Flask para gerenciar licenças de uso de software. Ideal para validar acessos, registrar máquinas e controlar o uso de sistemas licenciados de forma simples e eficiente.

📌 Objetivo
O projeto tem como finalidade fornecer uma API REST para autenticação e controle de licenças de sistemas. Pode ser utilizada por softwares comerciais que precisam validar o acesso por meio de um número de licença ou ID de máquina.

🛠️ Tecnologias Utilizadas
🐍 Python 3

🔧 Flask

🗂️ SQLite (ou outro banco de dados simples)

📦 Flask-Cors (para requisições externas)

📂 Estrutura do Projeto
licencas_api/
│
├── app.py                → Arquivo principal da API
├── database.db           → Banco de dados SQLite (ou gerado dinamicamente)
├── requirements.txt      → Dependências do projeto
├── /venv (opcional)      → Ambiente virtual

🚀 Funcionalidades da API

✅ Registro de novas licenças

🔍 Verificação de licença por máquina

⛔ Bloqueio de acesso se a licença for inválida

📊 (Opcional) Consulta de todas as licenças cadastradas

🔄 Atualização ou remoção de licenças (em desenvolvimento)

🧪 Endpoints (exemplos)
GET /verificar_licenca?codigo=ABC123&maquina=PC01
→ Verifica se a licença é válida para a máquina.

POST /registrar
→ Registra uma nova licença (com JSON no corpo da requisição).

👨‍💻 Autor
Henrique Liuti
Estudante de Ciência da Computação – 2º ano

📜 Licença
Este projeto é de uso acadêmico e profissional, com fins educacionais. Modificações e melhorias são bem-vindas.

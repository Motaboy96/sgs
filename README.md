# SISTEMA DE GERENCIAMENTO DE SEGURANÇA 

## DESCRIÇÃO 📝
Este sistema foi desenvolvido para gerenciar e monitorar produtos de segurança, incluindo veículos, equipamentos e dispositivos de segurança. Ele permite o controle de entradas e saídas de produtos, fornecendo métricas e gráficos para melhor visualização dos dados. 

## FUNCIONALIDADES 🚀
- Gerenciamento de recursos: Cadastro, edição e exclusão de produtos.
- Categorias: Classificação dos recursos em diferentes categorias.
- Controle de Estoque: Registra entradas e saídas de produtos.
- Dashboard: Exibição de dados resumidos
- Autenticação: Login e gestão de usuários e grupos com Django Admin.

## Tecnologias Utilizadas 🛠
- Backend: Django (Python)
- Frontend: HTML, CSS (BOOTSTRAP)
- Banco de Dados: SQLite

## Instrução de instalação ⚙️

### Clonar o repositório

```bash
git clone https://github.com/Motaboy96/sgs.git
cd sgs
```
### Criar e ativar ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  #Linux/Mac
venv\Scripts\activate  #Windows
```

### Instalar dependências
```bash
pip install -r requirements.txt
```

### Configurar o banco de dados
```bash
python manage.py migrate
python manage.py createsuperuser  # Criar um superusuário
```

### Iniciar o servidor
```bash
python manage.py runserver
```

## Instrução de uso  🖥️
### 1. Acesse o sistema de Gerenciamento em: http://127.0.0.1:8000/
- Aqui, você pode visualizar e gerenciar os recursos e atividades no sistema

### 2. Acesse o sistema de administração em: http://127.0.0.1:8000/admin
- Nesta área, é possivel gerenciar usuários, grupos e permissões

### 3. Faça o Login

### 4. Use o sistema

## Owner 👤
- Luan Mota
- Linkedin: https://www.linkedin.com/in/luan-mota-47b94a162/
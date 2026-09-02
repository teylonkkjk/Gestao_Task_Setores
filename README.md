
# 🏢 Sistema de Gestão de Tarefas e Dailies por Setor

Um sistema web completo desenvolvido em **Django** para o gerenciamento de tarefas (Tasks) e reuniões diárias (Daily Meetings) de uma empresa.

O grande diferencial deste projeto é a implementação robusta de **RBAC (Role-Based Access Control)**. O sistema não apenas gerencia dados, mas aplica regras de negócio reais, limitando ações com base no cargo hierárquico do usuário e em qual setor ele atua.

---

## ✨ Principais Funcionalidades

* **Sistema de Hierarquia e Cargos:** Usuários (`Membros`) possuem níveis de permissão específicos: Estagiário, Júnior, Sênior e Chefe de Setor.
* **Isolamento por Setores:** O Dashboard e os filtros garantem que um usuário só tenha acesso e interaja com as tarefas e Dailies pertinentes ao seu próprio departamento.
* **Gestão de Tarefas (Kanban-like):**
  * Criação, atribuição e deleção de tarefas.
  * Status dinâmicos: "A Fazer", "Em Processo", "Concluído".
* **Gestão de Reuniões (Dailies):**
  * Agendamento de Dailies por setor com links de chamadas e pautas.
  * `Daily Notes`: Cada membro pode registrar o que fez ontem, o planejamento de hoje e seus impedimentos.
* **Painel Administrativo Customizado:** O Django Admin foi fortemente sobrescrito para respeitar as regras de acesso dos cargos também no back-office.

---

## 🔒 Regras de Negócio Aplicadas (RBAC)

Para demonstrar conhecimento em regras de segurança e fluxo empresarial, as seguintes lógicas foram implementadas:

1. **Criação de Tarefas e Dailies:** Apenas usuários com nível **Sênior** ou **Chefe** podem criar novas tarefas ou agendar dailies para a equipe.
2. **Restrição de Conclusão:** Usuários de nível **Estagiário** conseguem mover tarefas para "Em Processo", mas o sistema bloqueia a transição para "Concluído" sem a validação de um cargo superior.
3. **Bloqueio Inter-setores:** Um membro de um setor não consegue visualizar, alterar o status ou interferir nas tarefas de um setor diferente do seu.
4. **Admin Seguro:** Permissões de Adição (`has_add_permission`), Edição (`has_change_permission`) e Exclusão (`has_delete_permission`) foram aplicadas direto no Admin. Só Seniores, Chefes e Superusers modificam a base estrutural.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Framework Web:** Django
* **Banco de Dados:** PostgreSQL
* **Autenticação:** Sistema nativo estendido (`AbstractUser`)
* **Front-end:** HTML5, Tailwind CSS, e Django Templates

---

## ⚙️ Como executar o projeto localmente

Siga os passos abaixo para testar a aplicação na sua máquina:

1. **Clone este repositório:**
   ```bash
   git clone [https://github.com/teylonkkjk/Gestao_Task_Setores.git](https://github.com/teylonkkjk/Gestao_Task_Setores.git)
   cd Gestao_Task_Setores
   ```

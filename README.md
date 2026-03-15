# Personal Command Center 🚀

Widget moderno e minimalista estilo Windows 11 para seu desktop.

## Funcionalidades

- 🌤️ **Clima** - Informações em tempo real da sua cidade
- ✅ **TODOs** - Gerencie suas tarefas do dia
- 🎯 **Foco do Dia** - Sugestão aleatória de hábito para focar
- 💡 **Motivação** - Frases inspiradoras diárias
- 📅 **Data** - Acompanhe o dia atual

## Instalação

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Execute o aplicativo:
```bash
python command_center.py
```

Ou simplesmente clique duas vezes em `run.bat`

## Configuração

Edite o arquivo `data/config.json` para personalizar sua cidade:

```json
{
  "city": "São Paulo",
  "country_code": "BR"
}
```

## Autostart no Windows

Para o Command Center abrir automaticamente ao ligar o PC:

1. Pressione `Win + R`
2. Digite `shell:startup` e pressione Enter
3. Copie o atalho `Command Center.lnk` para essa pasta

## Atalhos

- **ESC** - Fecha o widget
- **Arraste** - Mova o widget pela tela

## Personalizações Futuras

- Adicionar/editar TODOs direto no widget
- Integração com Google Calendar
- Temas customizáveis
- Notificações de lembretes

from telegram.ext import Updater, CommandHandler

def main():
    # Instanciamos el updater.
    updater = Updater(token="1296399086:AAHqkN2E-HHWfeYiHFLmprW3DpLgezknwRI", use_context=True)
    
    # Anyadiendo un manejador al comando /start
    updater.dispatcher.add_handler(CommandHandler("start", start))

    # Anyadir manejador para el comando /repite
    updater.dispatcher.add_handler(CommandHandler("repite", repite))

    # Suma dos numeros
    updater.dispatcher.add_handler(CommandHandler("suma", suma))

    # Empezamos a pedir notificaciones a Telegram.
    updater.start_polling()
    # Capturamos senyales de parada.
    updater.idle()

def start(update, context):
    update.message.repply_text("Hola soy un bot")

def repite(update, context):
    update.message.repply_text(update.message.text)

def suma(update, context):
    resultado = int(context.args[0]) + int(context.args[1])
    update.message.repply_text("Resultado", resultado)


if __name__ == '__main__':
    main()
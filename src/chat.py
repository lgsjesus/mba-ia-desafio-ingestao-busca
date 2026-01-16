from search import search_prompt
import sys
from pynput import keyboard

def on_press(key):
    if key == keyboard.Key.esc:
        print("\n\n[Saindo...] Até logo!")
        sys.exit(0)

def iniciar_cli():
    print("--- CLI de Perguntas ---")
    print("Instruções: Digite sua pergunta e aperte Enter.")
    print("Pressione 'Esc' a qualquer momento para sair.\n")
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    try:
        while True:
            pergunta = input("Fazer pergunta: ")
            
            if pergunta.strip():
                print(f"Processando: '{pergunta}'...\n")
                resposta = search_prompt(pergunta)
                print(f"Resposta: {resposta}\n") 

            else:
                print("Por favor, digite algo ou Esc para sair.")
                
    except KeyboardInterrupt:
        # Lida com Ctrl+C
        print("\nEncerrado.")

if __name__ == "__main__":
    iniciar_cli()
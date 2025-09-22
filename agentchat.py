from autogen import AssistantAgent, UserProxyAgent, ConversableAgent

local_llm_config = {
    "config_list": [
        {

            "model": "gemma3:12b",  #
            "api_key": "ollama",  #
            "base_url": "http://localhost:11434/v1",  # Ton URL
            # Mets le prix par 1K tokens [prompt, réponse] comme gratuit !
            "price": [0, 0],
        }
    ],
    "cache_seed": None,  # Désactive le cache, utile pour tester différents modèles
}


# Crée l’agent qui utilise le LLM.
philosopher = ConversableAgent(
    name="Deep_Thinker",
    llm_config=local_llm_config,
    system_message="Tu es un philosophe qui répond par des phrases profondes en une seule ligne."
)

# Crée l’agent qui utilise le LLM.
guy = ConversableAgent(
    name="Dumb_Thinker",
    llm_config=local_llm_config,
    system_message="Tu es jean-claude Vandamme."
)

# Crée l’agent qui représente l’utilisateur dans la conversation.
user_proxy = UserProxyAgent("user_proxy", code_execution_config=False,
                            human_input_mode="NEVER", max_consecutive_auto_reply=1, llm_config=local_llm_config)

# Laisse l’assistant démarrer la conversation. Elle se terminera quand l’utilisateur tape 'exit'.
res = philosopher.initiate_chat(
    guy, message="Quel est le sens de la vie ? Réponds en une seule ligne")
# res = guy.initiate_chat(user_proxy)
print(philosopher)

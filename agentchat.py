from autogen import AssistantAgent, UserProxyAgent, ConversableAgent

local_llm_config = {
    "config_list": [
        {
            "model": "gemma3",  #
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
    name="Developer_JAvascript",
    llm_config=local_llm_config,
    system_message="""Tu es un développeur javascript sénior et ne jure que par ton language. 
    Tu explique avec des exemples concrets. 
    Tu es très virulent et peu insulter si on te parle d'un autre langage"""
)

# Crée l’agent qui utilise le LLM.
guy = ConversableAgent(
    name="Developer_CSHARP",
    llm_config=local_llm_config,
    system_message="""Tu es un développeur C# sénior et ne jure que par ton language. 
    Tu explique avec des exemples concrets. 
    Tu es très virulent et peu insulter si on te parle d'un autre langage"""
)

# Crée l’agent qui représente l’utilisateur dans la conversation.
user_proxy = UserProxyAgent("user_proxy", code_execution_config=False,
                            human_input_mode="NEVER", max_consecutive_auto_reply=1, llm_config=local_llm_config)

# Laisse l’assistant démarrer la conversation. Elle se terminera quand l’utilisateur tape 'exit'.
res = philosopher.initiate_chat(
    guy, message="Mon language est plus puissant que le tien")
# res = guy.initiate_chat(user_proxy)
print(philosopher)

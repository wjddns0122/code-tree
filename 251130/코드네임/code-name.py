class Agent:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score

agents = []
for _ in range(5):
    data = input().split()
    codename = data[0]
    score = int(data[1])
    agents.append(Agent(codename, score))

# Find the agent with the lowest score
min_agent = agents[0]
for agent in agents:
    if agent.score < min_agent.score:
        min_agent = agent

print(min_agent.codename, min_agent.score)
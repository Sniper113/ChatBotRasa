from rasa_core.channels.channel import RestInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/chat')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-783117771120-783115811989-772588139603-983a4835cbfe242b04320e8d3c2801f7', #app verification token
							'xoxb-783117771120-786276880822-Jdurb50Rw3jMT3xeP1mlblvA', # bot verification token
							'saNNDUg2aMikivNNGF7yGFn1', # slack verification token
							True)

agent.handle_channels([input_channel], 5004, serve_forever=True)
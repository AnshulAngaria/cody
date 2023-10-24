import os
import openai


openai.api_key = open("api_key.txt").read().strip()

system_prompt = "You are a coding agent. You will be give some task to edit code or add code in a file.\
You will have to return a bash command to perform that task. You will be provided the output of the command by the user. You have to \
output only the bash command and no other text. Do not interact with the user. You command should be able to run on bash. You cannot use interactive\
text editors like vim, you have use only command line to edit files."

message=[
		{
		"role": "system",
		"content": system_prompt
		}
	]
user_input = input("User - ")
message.append({
	"role": "user",
	"content": user_input
})

while True:
	print("Sending request ", message)
	response = openai.ChatCompletion.create(
	model="gpt-3.5-turbo",
	messages=message,
	temperature=1,
	max_tokens=256,
	top_p=1,
	frequency_penalty=0,
	presence_penalty=0
	)
	command = response["choices"][0]["message"]["content"]
	print('Got command ', response["choices"][0]["message"]["content"])
	input("Execute command, Press enter or ctrl+c")
	output = os.popen(command).read()

	print("Output: ", output)
	message.append({
		"role": "assistant",
		"content": command
	})
	if output != '':
		message.append({
			"role": "user",
			"content": output
		})
	

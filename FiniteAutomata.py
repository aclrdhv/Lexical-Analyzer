def checkString(input_string,string_rules):
    current_state = "q0"

    transition = {}

    for x in range(0,len(string_rules)):
        transition[f"q{x}"] = {
                string_rules[x]: f"q{x+1}",
                "eos": "error"
            }
        
    transition[f"q{len(string_rules)}"] = {
            f"q{len(string_rules)}": f"q{len(string_rules)}",
            "eos": "accept"
        }
    
    transition["qerror"] = {
            "qerror": "qerror",
            "eos": "error"
        }
    
    for char in input_string:
        if char in transition[current_state]:
            current_state = transition[current_state][char]
        else:
            current_state = transition["qerror"]["qerror"]

    return transition[current_state]["eos"] == "accept"
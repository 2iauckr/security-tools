class beautyConsole:
    """This class defines properties and methods to manipulate console output"""
    colors = {
        "black": '\33[30m',
        "red": '\33[31m',
        "green": '\33[32m',
        "yellow": '\33[33m',
        "blue": '\33[34m',
        "magenta": '\33[35m',
        "cyan": '\33[36m',
        "white": '\33[37m',
        "grey": '\33[90m',
        "lightblue": '\33[94m'
    }

    characters = {
        "endline": '\33[0m'
    }

    def __init__(self):
        return None

    @staticmethod
    def getColor(color_name):
        """returns color identified by color_name or white as default value"""
        if color_name in beautyConsole.colors:
            return beautyConsole.colors[color_name]
        return beautyConsole.colors["white"]

    @staticmethod
    def getSpecialChar(char_name):
        """returns special character identified by char_name"""
        if char_name in beautyConsole.characters:
            return beautyConsole.characters[char_name]
        return ""


    efMsgFound = " - potential vulnerable code"
    eKeyWordFound = "keyword with possibly critical meaning in code"
    efMsgGlobalFound = "global variable explicit call"
    fiMsgFound = "file include pattern found; potential LFI/RFI detected"
    eReflFound = "reflected property found; check for XSS"

from typing import List
"""
Given a 2D board and a list of words from the dictionary, find all words in the board.
Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word
"""


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        class TrieNode:
            def __init__(self) -> None:
                self.vals = [None] * (ord('z') - ord('a') + 1)
                self.end = False

        class Trie:
            def __init__(self):
                self.root = TrieNode()

            def getIndex(self, char) -> int:
                return ord(char) - ord('a')

            def addWord(self, word: str) -> None:
                cur = self.root
                for c in word:
                    pos = self.getIndex(c)
                    if cur.vals[pos] == None:
                        newNode = TrieNode()
                        cur.vals[pos] = newNode
                        cur = newNode
                    else:
                        cur = cur.vals[pos]
                cur.end = True

            def showWords(self) -> None:
                words = []

                def getWords(curNode: TrieNode, word: str) -> None:
                    nonlocal words
                    for i, node in enumerate(curNode.vals):
                        if node != None:
                            ch = ord('a') + i
                            if node.end == True:
                                words.append(word + chr(ch))
                            getWords(node, word + chr(ch))

                getWords(self.root, "")
                print(words)

        trie = Trie()
        for w in words:
            trie.addWord(w)

        def dfs(board, node, word, i, j, ans):

            if node.end:
                node.end = False
                ans.add(word)

            if i < 0 or i > len(board) - 1 or j < 0 or j > len(board[i]) - 1:
                return

            c = board[i][j]

            newNode = None
            if ord(c) - ord('a') in range(27):
                newNode = node.vals[ord(c) - ord('a')]

            if (newNode == None):
                return

            board[i][j] = "#"

            dfs(board, newNode, word + c, i - 1, j, ans)
            dfs(board, newNode, word + c, i + 1, j, ans)
            dfs(board, newNode, word + c, i, j - 1, ans)
            dfs(board, newNode, word + c, i, j + 1, ans)

            board[i][j] = c

        ans = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                dfs(board, trie.root, "", i, j, ans)
        # print(board)
        # print(ans)
        return sorted(list(ans))

    def test(self):
        assert self.findWords(board=[['o', 'a', 'a',
                                      'n'], ['e', 't', 'a', 'e'],
                                     ['i', 'h', 'k', 'r'],
                                     ['i', 'f', 'l', 'v']],
                              words=["oath", "pea", "eat",
                                     "rain"]) == ["eat", "oath"]
        assert self.findWords(
            board=[["a", "a", "a", "a"], ["a", "a", "a", "a"],
                   ["a", "a", "a",
                    "a"], ["a", "a", "a",
                           "a"], ["b", "c", "d",
                                  "e"],
                   ["f",
                    "g", "h", "i"], ["j", "k", "l",
                                     "m"], ["n", "o", "p",
                                            "q"],
                   ["r", "s", "t",
                    "u"], ["v", "w", "x",
                           "y"], ["z", "z", "z",
                                  "z"]],
            words=[
                "aaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaab", "aaaaaaaaaaaaaaac",
                "aaaaaaaaaaaaaaad", "aaaaaaaaaaaaaaae", "aaaaaaaaaaaaaaaf",
                "aaaaaaaaaaaaaaag", "aaaaaaaaaaaaaaah", "aaaaaaaaaaaaaaai",
                "aaaaaaaaaaaaaaaj", "aaaaaaaaaaaaaaak", "aaaaaaaaaaaaaaal",
                "aaaaaaaaaaaaaaam", "aaaaaaaaaaaaaaan", "aaaaaaaaaaaaaaao",
                "aaaaaaaaaaaaaaap", "aaaaaaaaaaaaaaaq", "aaaaaaaaaaaaaaar",
                "aaaaaaaaaaaaaaas", "aaaaaaaaaaaaaaat", "aaaaaaaaaaaaaaau",
                "aaaaaaaaaaaaaaav", "aaaaaaaaaaaaaaaw", "aaaaaaaaaaaaaaax",
                "aaaaaaaaaaaaaaay", "aaaaaaaaaaaaaaaz", "aaaaaaaaaaaaaaba",
                "aaaaaaaaaaaaaabb", "aaaaaaaaaaaaaabc", "aaaaaaaaaaaaaabd",
                "aaaaaaaaaaaaaabe", "aaaaaaaaaaaaaabf", "aaaaaaaaaaaaaabg",
                "aaaaaaaaaaaaaabh", "aaaaaaaaaaaaaabi", "aaaaaaaaaaaaaabj",
                "aaaaaaaaaaaaaabk", "aaaaaaaaaaaaaabl", "aaaaaaaaaaaaaabm",
                "aaaaaaaaaaaaaabn", "aaaaaaaaaaaaaabo", "aaaaaaaaaaaaaabp",
                "aaaaaaaaaaaaaabq", "aaaaaaaaaaaaaabr", "aaaaaaaaaaaaaabs",
                "aaaaaaaaaaaaaabt", "aaaaaaaaaaaaaabu", "aaaaaaaaaaaaaabv",
                "aaaaaaaaaaaaaabw", "aaaaaaaaaaaaaabx", "aaaaaaaaaaaaaaby",
                "aaaaaaaaaaaaaabz", "aaaaaaaaaaaaaaca", "aaaaaaaaaaaaaacb",
                "aaaaaaaaaaaaaacc", "aaaaaaaaaaaaaacd", "aaaaaaaaaaaaaace",
                "aaaaaaaaaaaaaacf", "aaaaaaaaaaaaaacg", "aaaaaaaaaaaaaach",
                "aaaaaaaaaaaaaaci", "aaaaaaaaaaaaaacj", "aaaaaaaaaaaaaack",
                "aaaaaaaaaaaaaacl", "aaaaaaaaaaaaaacm", "aaaaaaaaaaaaaacn",
                "aaaaaaaaaaaaaaco", "aaaaaaaaaaaaaacp", "aaaaaaaaaaaaaacq",
                "aaaaaaaaaaaaaacr", "aaaaaaaaaaaaaacs", "aaaaaaaaaaaaaact",
                "aaaaaaaaaaaaaacu", "aaaaaaaaaaaaaacv", "aaaaaaaaaaaaaacw",
                "aaaaaaaaaaaaaacx", "aaaaaaaaaaaaaacy", "aaaaaaaaaaaaaacz",
                "aaaaaaaaaaaaaada", "aaaaaaaaaaaaaadb", "aaaaaaaaaaaaaadc",
                "aaaaaaaaaaaaaadd", "aaaaaaaaaaaaaade", "aaaaaaaaaaaaaadf",
                "aaaaaaaaaaaaaadg", "aaaaaaaaaaaaaadh", "aaaaaaaaaaaaaadi",
                "aaaaaaaaaaaaaadj", "aaaaaaaaaaaaaadk", "aaaaaaaaaaaaaadl",
                "aaaaaaaaaaaaaadm", "aaaaaaaaaaaaaadn", "aaaaaaaaaaaaaado",
                "aaaaaaaaaaaaaadp", "aaaaaaaaaaaaaadq", "aaaaaaaaaaaaaadr",
                "aaaaaaaaaaaaaads", "aaaaaaaaaaaaaadt", "aaaaaaaaaaaaaadu",
                "aaaaaaaaaaaaaadv", "aaaaaaaaaaaaaadw", "aaaaaaaaaaaaaadx",
                "aaaaaaaaaaaaaady", "aaaaaaaaaaaaaadz", "aaaaaaaaaaaaaaea",
                "aaaaaaaaaaaaaaeb", "aaaaaaaaaaaaaaec", "aaaaaaaaaaaaaaed",
                "aaaaaaaaaaaaaaee", "aaaaaaaaaaaaaaef", "aaaaaaaaaaaaaaeg",
                "aaaaaaaaaaaaaaeh", "aaaaaaaaaaaaaaei", "aaaaaaaaaaaaaaej",
                "aaaaaaaaaaaaaaek", "aaaaaaaaaaaaaael", "aaaaaaaaaaaaaaem",
                "aaaaaaaaaaaaaaen", "aaaaaaaaaaaaaaeo", "aaaaaaaaaaaaaaep",
                "aaaaaaaaaaaaaaeq", "aaaaaaaaaaaaaaer", "aaaaaaaaaaaaaaes",
                "aaaaaaaaaaaaaaet", "aaaaaaaaaaaaaaeu", "aaaaaaaaaaaaaaev",
                "aaaaaaaaaaaaaaew", "aaaaaaaaaaaaaaex", "aaaaaaaaaaaaaaey",
                "aaaaaaaaaaaaaaez", "aaaaaaaaaaaaaafa", "aaaaaaaaaaaaaafb",
                "aaaaaaaaaaaaaafc", "aaaaaaaaaaaaaafd", "aaaaaaaaaaaaaafe",
                "aaaaaaaaaaaaaaff", "aaaaaaaaaaaaaafg", "aaaaaaaaaaaaaafh",
                "aaaaaaaaaaaaaafi", "aaaaaaaaaaaaaafj", "aaaaaaaaaaaaaafk",
                "aaaaaaaaaaaaaafl", "aaaaaaaaaaaaaafm", "aaaaaaaaaaaaaafn",
                "aaaaaaaaaaaaaafo", "aaaaaaaaaaaaaafp", "aaaaaaaaaaaaaafq",
                "aaaaaaaaaaaaaafr", "aaaaaaaaaaaaaafs", "aaaaaaaaaaaaaaft",
                "aaaaaaaaaaaaaafu", "aaaaaaaaaaaaaafv", "aaaaaaaaaaaaaafw",
                "aaaaaaaaaaaaaafx", "aaaaaaaaaaaaaafy", "aaaaaaaaaaaaaafz",
                "aaaaaaaaaaaaaaga", "aaaaaaaaaaaaaagb", "aaaaaaaaaaaaaagc",
                "aaaaaaaaaaaaaagd", "aaaaaaaaaaaaaage", "aaaaaaaaaaaaaagf",
                "aaaaaaaaaaaaaagg", "aaaaaaaaaaaaaagh", "aaaaaaaaaaaaaagi",
                "aaaaaaaaaaaaaagj", "aaaaaaaaaaaaaagk", "aaaaaaaaaaaaaagl",
                "aaaaaaaaaaaaaagm", "aaaaaaaaaaaaaagn", "aaaaaaaaaaaaaago",
                "aaaaaaaaaaaaaagp", "aaaaaaaaaaaaaagq", "aaaaaaaaaaaaaagr",
                "aaaaaaaaaaaaaags", "aaaaaaaaaaaaaagt", "aaaaaaaaaaaaaagu",
                "aaaaaaaaaaaaaagv", "aaaaaaaaaaaaaagw", "aaaaaaaaaaaaaagx",
                "aaaaaaaaaaaaaagy", "aaaaaaaaaaaaaagz", "aaaaaaaaaaaaaaha",
                "aaaaaaaaaaaaaahb", "aaaaaaaaaaaaaahc", "aaaaaaaaaaaaaahd",
                "aaaaaaaaaaaaaahe", "aaaaaaaaaaaaaahf", "aaaaaaaaaaaaaahg",
                "aaaaaaaaaaaaaahh", "aaaaaaaaaaaaaahi", "aaaaaaaaaaaaaahj",
                "aaaaaaaaaaaaaahk", "aaaaaaaaaaaaaahl", "aaaaaaaaaaaaaahm",
                "aaaaaaaaaaaaaahn", "aaaaaaaaaaaaaaho", "aaaaaaaaaaaaaahp",
                "aaaaaaaaaaaaaahq", "aaaaaaaaaaaaaahr", "aaaaaaaaaaaaaahs",
                "aaaaaaaaaaaaaaht", "aaaaaaaaaaaaaahu", "aaaaaaaaaaaaaahv",
                "aaaaaaaaaaaaaahw", "aaaaaaaaaaaaaahx", "aaaaaaaaaaaaaahy",
                "aaaaaaaaaaaaaahz", "aaaaaaaaaaaaaaia", "aaaaaaaaaaaaaaib",
                "aaaaaaaaaaaaaaic", "aaaaaaaaaaaaaaid", "aaaaaaaaaaaaaaie",
                "aaaaaaaaaaaaaaif", "aaaaaaaaaaaaaaig", "aaaaaaaaaaaaaaih",
                "aaaaaaaaaaaaaaii", "aaaaaaaaaaaaaaij", "aaaaaaaaaaaaaaik",
                "aaaaaaaaaaaaaail", "aaaaaaaaaaaaaaim", "aaaaaaaaaaaaaain",
                "aaaaaaaaaaaaaaio", "aaaaaaaaaaaaaaip", "aaaaaaaaaaaaaaiq",
                "aaaaaaaaaaaaaair", "aaaaaaaaaaaaaais", "aaaaaaaaaaaaaait",
                "aaaaaaaaaaaaaaiu", "aaaaaaaaaaaaaaiv", "aaaaaaaaaaaaaaiw",
                "aaaaaaaaaaaaaaix", "aaaaaaaaaaaaaaiy", "aaaaaaaaaaaaaaiz",
                "aaaaaaaaaaaaaaja", "aaaaaaaaaaaaaajb", "aaaaaaaaaaaaaajc",
                "aaaaaaaaaaaaaajd", "aaaaaaaaaaaaaaje", "aaaaaaaaaaaaaajf",
                "aaaaaaaaaaaaaajg", "aaaaaaaaaaaaaajh", "aaaaaaaaaaaaaaji",
                "aaaaaaaaaaaaaajj", "aaaaaaaaaaaaaajk", "aaaaaaaaaaaaaajl",
                "aaaaaaaaaaaaaajm", "aaaaaaaaaaaaaajn", "aaaaaaaaaaaaaajo",
                "aaaaaaaaaaaaaajp", "aaaaaaaaaaaaaajq", "aaaaaaaaaaaaaajr",
                "aaaaaaaaaaaaaajs", "aaaaaaaaaaaaaajt", "aaaaaaaaaaaaaaju",
                "aaaaaaaaaaaaaajv", "aaaaaaaaaaaaaajw", "aaaaaaaaaaaaaajx",
                "aaaaaaaaaaaaaajy", "aaaaaaaaaaaaaajz", "aaaaaaaaaaaaaaka",
                "aaaaaaaaaaaaaakb", "aaaaaaaaaaaaaakc", "aaaaaaaaaaaaaakd",
                "aaaaaaaaaaaaaake", "aaaaaaaaaaaaaakf", "aaaaaaaaaaaaaakg",
                "aaaaaaaaaaaaaakh", "aaaaaaaaaaaaaaki", "aaaaaaaaaaaaaakj",
                "aaaaaaaaaaaaaakk", "aaaaaaaaaaaaaakl", "aaaaaaaaaaaaaakm",
                "aaaaaaaaaaaaaakn", "aaaaaaaaaaaaaako", "aaaaaaaaaaaaaakp",
                "aaaaaaaaaaaaaakq", "aaaaaaaaaaaaaakr", "aaaaaaaaaaaaaaks",
                "aaaaaaaaaaaaaakt", "aaaaaaaaaaaaaaku", "aaaaaaaaaaaaaakv",
                "aaaaaaaaaaaaaakw", "aaaaaaaaaaaaaakx", "aaaaaaaaaaaaaaky",
                "aaaaaaaaaaaaaakz", "aaaaaaaaaaaaaala", "aaaaaaaaaaaaaalb",
                "aaaaaaaaaaaaaalc", "aaaaaaaaaaaaaald", "aaaaaaaaaaaaaale",
                "aaaaaaaaaaaaaalf", "aaaaaaaaaaaaaalg", "aaaaaaaaaaaaaalh",
                "aaaaaaaaaaaaaali", "aaaaaaaaaaaaaalj", "aaaaaaaaaaaaaalk",
                "aaaaaaaaaaaaaall", "aaaaaaaaaaaaaalm", "aaaaaaaaaaaaaaln",
                "aaaaaaaaaaaaaalo", "aaaaaaaaaaaaaalp", "aaaaaaaaaaaaaalq",
                "aaaaaaaaaaaaaalr", "aaaaaaaaaaaaaals", "aaaaaaaaaaaaaalt",
                "aaaaaaaaaaaaaalu", "aaaaaaaaaaaaaalv", "aaaaaaaaaaaaaalw",
                "aaaaaaaaaaaaaalx", "aaaaaaaaaaaaaaly", "aaaaaaaaaaaaaalz",
                "aaaaaaaaaaaaaama", "aaaaaaaaaaaaaamb", "aaaaaaaaaaaaaamc",
                "aaaaaaaaaaaaaamd", "aaaaaaaaaaaaaame", "aaaaaaaaaaaaaamf",
                "aaaaaaaaaaaaaamg", "aaaaaaaaaaaaaamh", "aaaaaaaaaaaaaami",
                "aaaaaaaaaaaaaamj", "aaaaaaaaaaaaaamk", "aaaaaaaaaaaaaaml",
                "aaaaaaaaaaaaaamm", "aaaaaaaaaaaaaamn", "aaaaaaaaaaaaaamo",
                "aaaaaaaaaaaaaamp", "aaaaaaaaaaaaaamq", "aaaaaaaaaaaaaamr",
                "aaaaaaaaaaaaaams", "aaaaaaaaaaaaaamt", "aaaaaaaaaaaaaamu",
                "aaaaaaaaaaaaaamv", "aaaaaaaaaaaaaamw", "aaaaaaaaaaaaaamx",
                "aaaaaaaaaaaaaamy", "aaaaaaaaaaaaaamz", "aaaaaaaaaaaaaana",
                "aaaaaaaaaaaaaanb", "aaaaaaaaaaaaaanc", "aaaaaaaaaaaaaand",
                "aaaaaaaaaaaaaane", "aaaaaaaaaaaaaanf", "aaaaaaaaaaaaaang",
                "aaaaaaaaaaaaaanh", "aaaaaaaaaaaaaani", "aaaaaaaaaaaaaanj",
                "aaaaaaaaaaaaaank", "aaaaaaaaaaaaaanl", "aaaaaaaaaaaaaanm",
                "aaaaaaaaaaaaaann", "aaaaaaaaaaaaaano", "aaaaaaaaaaaaaanp",
                "aaaaaaaaaaaaaanq", "aaaaaaaaaaaaaanr", "aaaaaaaaaaaaaans",
                "aaaaaaaaaaaaaant", "aaaaaaaaaaaaaanu", "aaaaaaaaaaaaaanv",
                "aaaaaaaaaaaaaanw", "aaaaaaaaaaaaaanx", "aaaaaaaaaaaaaany",
                "aaaaaaaaaaaaaanz", "aaaaaaaaaaaaaaoa", "aaaaaaaaaaaaaaob",
                "aaaaaaaaaaaaaaoc", "aaaaaaaaaaaaaaod", "aaaaaaaaaaaaaaoe",
                "aaaaaaaaaaaaaaof", "aaaaaaaaaaaaaaog", "aaaaaaaaaaaaaaoh",
                "aaaaaaaaaaaaaaoi", "aaaaaaaaaaaaaaoj", "aaaaaaaaaaaaaaok",
                "aaaaaaaaaaaaaaol", "aaaaaaaaaaaaaaom", "aaaaaaaaaaaaaaon",
                "aaaaaaaaaaaaaaoo", "aaaaaaaaaaaaaaop", "aaaaaaaaaaaaaaoq",
                "aaaaaaaaaaaaaaor", "aaaaaaaaaaaaaaos", "aaaaaaaaaaaaaaot",
                "aaaaaaaaaaaaaaou", "aaaaaaaaaaaaaaov", "aaaaaaaaaaaaaaow",
                "aaaaaaaaaaaaaaox", "aaaaaaaaaaaaaaoy", "aaaaaaaaaaaaaaoz",
                "aaaaaaaaaaaaaapa", "aaaaaaaaaaaaaapb", "aaaaaaaaaaaaaapc",
                "aaaaaaaaaaaaaapd", "aaaaaaaaaaaaaape", "aaaaaaaaaaaaaapf",
                "aaaaaaaaaaaaaapg", "aaaaaaaaaaaaaaph", "aaaaaaaaaaaaaapi",
                "aaaaaaaaaaaaaapj", "aaaaaaaaaaaaaapk", "aaaaaaaaaaaaaapl",
                "aaaaaaaaaaaaaapm", "aaaaaaaaaaaaaapn", "aaaaaaaaaaaaaapo",
                "aaaaaaaaaaaaaapp", "aaaaaaaaaaaaaapq", "aaaaaaaaaaaaaapr",
                "aaaaaaaaaaaaaaps", "aaaaaaaaaaaaaapt", "aaaaaaaaaaaaaapu",
                "aaaaaaaaaaaaaapv", "aaaaaaaaaaaaaapw", "aaaaaaaaaaaaaapx",
                "aaaaaaaaaaaaaapy", "aaaaaaaaaaaaaapz", "aaaaaaaaaaaaaaqa",
                "aaaaaaaaaaaaaaqb", "aaaaaaaaaaaaaaqc", "aaaaaaaaaaaaaaqd",
                "aaaaaaaaaaaaaaqe", "aaaaaaaaaaaaaaqf", "aaaaaaaaaaaaaaqg",
                "aaaaaaaaaaaaaaqh", "aaaaaaaaaaaaaaqi", "aaaaaaaaaaaaaaqj",
                "aaaaaaaaaaaaaaqk", "aaaaaaaaaaaaaaql", "aaaaaaaaaaaaaaqm",
                "aaaaaaaaaaaaaaqn", "aaaaaaaaaaaaaaqo", "aaaaaaaaaaaaaaqp",
                "aaaaaaaaaaaaaaqq", "aaaaaaaaaaaaaaqr", "aaaaaaaaaaaaaaqs",
                "aaaaaaaaaaaaaaqt", "aaaaaaaaaaaaaaqu", "aaaaaaaaaaaaaaqv",
                "aaaaaaaaaaaaaaqw", "aaaaaaaaaaaaaaqx", "aaaaaaaaaaaaaaqy",
                "aaaaaaaaaaaaaaqz", "aaaaaaaaaaaaaara", "aaaaaaaaaaaaaarb",
                "aaaaaaaaaaaaaarc", "aaaaaaaaaaaaaard", "aaaaaaaaaaaaaare",
                "aaaaaaaaaaaaaarf", "aaaaaaaaaaaaaarg", "aaaaaaaaaaaaaarh",
                "aaaaaaaaaaaaaari", "aaaaaaaaaaaaaarj", "aaaaaaaaaaaaaark",
                "aaaaaaaaaaaaaarl", "aaaaaaaaaaaaaarm", "aaaaaaaaaaaaaarn",
                "aaaaaaaaaaaaaaro", "aaaaaaaaaaaaaarp", "aaaaaaaaaaaaaarq",
                "aaaaaaaaaaaaaarr", "aaaaaaaaaaaaaars", "aaaaaaaaaaaaaart",
                "aaaaaaaaaaaaaaru", "aaaaaaaaaaaaaarv", "aaaaaaaaaaaaaarw",
                "aaaaaaaaaaaaaarx", "aaaaaaaaaaaaaary", "aaaaaaaaaaaaaarz",
                "aaaaaaaaaaaaaasa", "aaaaaaaaaaaaaasb", "aaaaaaaaaaaaaasc",
                "aaaaaaaaaaaaaasd", "aaaaaaaaaaaaaase", "aaaaaaaaaaaaaasf",
                "aaaaaaaaaaaaaasg", "aaaaaaaaaaaaaash", "aaaaaaaaaaaaaasi",
                "aaaaaaaaaaaaaasj", "aaaaaaaaaaaaaask", "aaaaaaaaaaaaaasl",
                "aaaaaaaaaaaaaasm", "aaaaaaaaaaaaaasn", "aaaaaaaaaaaaaaso",
                "aaaaaaaaaaaaaasp", "aaaaaaaaaaaaaasq", "aaaaaaaaaaaaaasr",
                "aaaaaaaaaaaaaass", "aaaaaaaaaaaaaast", "aaaaaaaaaaaaaasu",
                "aaaaaaaaaaaaaasv", "aaaaaaaaaaaaaasw", "aaaaaaaaaaaaaasx",
                "aaaaaaaaaaaaaasy", "aaaaaaaaaaaaaasz", "aaaaaaaaaaaaaata",
                "aaaaaaaaaaaaaatb", "aaaaaaaaaaaaaatc", "aaaaaaaaaaaaaatd",
                "aaaaaaaaaaaaaate", "aaaaaaaaaaaaaatf", "aaaaaaaaaaaaaatg",
                "aaaaaaaaaaaaaath", "aaaaaaaaaaaaaati", "aaaaaaaaaaaaaatj",
                "aaaaaaaaaaaaaatk", "aaaaaaaaaaaaaatl", "aaaaaaaaaaaaaatm",
                "aaaaaaaaaaaaaatn", "aaaaaaaaaaaaaato", "aaaaaaaaaaaaaatp",
                "aaaaaaaaaaaaaatq", "aaaaaaaaaaaaaatr", "aaaaaaaaaaaaaats",
                "aaaaaaaaaaaaaatt", "aaaaaaaaaaaaaatu", "aaaaaaaaaaaaaatv",
                "aaaaaaaaaaaaaatw", "aaaaaaaaaaaaaatx", "aaaaaaaaaaaaaaty",
                "aaaaaaaaaaaaaatz", "aaaaaaaaaaaaaaua", "aaaaaaaaaaaaaaub",
                "aaaaaaaaaaaaaauc", "aaaaaaaaaaaaaaud", "aaaaaaaaaaaaaaue",
                "aaaaaaaaaaaaaauf", "aaaaaaaaaaaaaaug", "aaaaaaaaaaaaaauh",
                "aaaaaaaaaaaaaaui", "aaaaaaaaaaaaaauj", "aaaaaaaaaaaaaauk",
                "aaaaaaaaaaaaaaul", "aaaaaaaaaaaaaaum", "aaaaaaaaaaaaaaun",
                "aaaaaaaaaaaaaauo", "aaaaaaaaaaaaaaup", "aaaaaaaaaaaaaauq",
                "aaaaaaaaaaaaaaur", "aaaaaaaaaaaaaaus", "aaaaaaaaaaaaaaut",
                "aaaaaaaaaaaaaauu", "aaaaaaaaaaaaaauv", "aaaaaaaaaaaaaauw",
                "aaaaaaaaaaaaaaux", "aaaaaaaaaaaaaauy", "aaaaaaaaaaaaaauz",
                "aaaaaaaaaaaaaava", "aaaaaaaaaaaaaavb", "aaaaaaaaaaaaaavc",
                "aaaaaaaaaaaaaavd", "aaaaaaaaaaaaaave", "aaaaaaaaaaaaaavf",
                "aaaaaaaaaaaaaavg", "aaaaaaaaaaaaaavh", "aaaaaaaaaaaaaavi",
                "aaaaaaaaaaaaaavj", "aaaaaaaaaaaaaavk", "aaaaaaaaaaaaaavl",
                "aaaaaaaaaaaaaavm", "aaaaaaaaaaaaaavn", "aaaaaaaaaaaaaavo",
                "aaaaaaaaaaaaaavp", "aaaaaaaaaaaaaavq", "aaaaaaaaaaaaaavr",
                "aaaaaaaaaaaaaavs", "aaaaaaaaaaaaaavt", "aaaaaaaaaaaaaavu",
                "aaaaaaaaaaaaaavv", "aaaaaaaaaaaaaavw", "aaaaaaaaaaaaaavx",
                "aaaaaaaaaaaaaavy", "aaaaaaaaaaaaaavz", "aaaaaaaaaaaaaawa",
                "aaaaaaaaaaaaaawb", "aaaaaaaaaaaaaawc", "aaaaaaaaaaaaaawd",
                "aaaaaaaaaaaaaawe", "aaaaaaaaaaaaaawf", "aaaaaaaaaaaaaawg",
                "aaaaaaaaaaaaaawh", "aaaaaaaaaaaaaawi", "aaaaaaaaaaaaaawj",
                "aaaaaaaaaaaaaawk", "aaaaaaaaaaaaaawl", "aaaaaaaaaaaaaawm",
                "aaaaaaaaaaaaaawn", "aaaaaaaaaaaaaawo", "aaaaaaaaaaaaaawp",
                "aaaaaaaaaaaaaawq", "aaaaaaaaaaaaaawr", "aaaaaaaaaaaaaaws",
                "aaaaaaaaaaaaaawt", "aaaaaaaaaaaaaawu", "aaaaaaaaaaaaaawv",
                "aaaaaaaaaaaaaaww", "aaaaaaaaaaaaaawx", "aaaaaaaaaaaaaawy",
                "aaaaaaaaaaaaaawz", "aaaaaaaaaaaaaaxa", "aaaaaaaaaaaaaaxb",
                "aaaaaaaaaaaaaaxc", "aaaaaaaaaaaaaaxd", "aaaaaaaaaaaaaaxe",
                "aaaaaaaaaaaaaaxf", "aaaaaaaaaaaaaaxg", "aaaaaaaaaaaaaaxh",
                "aaaaaaaaaaaaaaxi", "aaaaaaaaaaaaaaxj", "aaaaaaaaaaaaaaxk",
                "aaaaaaaaaaaaaaxl", "aaaaaaaaaaaaaaxm", "aaaaaaaaaaaaaaxn",
                "aaaaaaaaaaaaaaxo", "aaaaaaaaaaaaaaxp", "aaaaaaaaaaaaaaxq",
                "aaaaaaaaaaaaaaxr", "aaaaaaaaaaaaaaxs", "aaaaaaaaaaaaaaxt",
                "aaaaaaaaaaaaaaxu", "aaaaaaaaaaaaaaxv", "aaaaaaaaaaaaaaxw",
                "aaaaaaaaaaaaaaxx", "aaaaaaaaaaaaaaxy", "aaaaaaaaaaaaaaxz",
                "aaaaaaaaaaaaaaya", "aaaaaaaaaaaaaayb", "aaaaaaaaaaaaaayc",
                "aaaaaaaaaaaaaayd", "aaaaaaaaaaaaaaye", "aaaaaaaaaaaaaayf",
                "aaaaaaaaaaaaaayg", "aaaaaaaaaaaaaayh", "aaaaaaaaaaaaaayi",
                "aaaaaaaaaaaaaayj", "aaaaaaaaaaaaaayk", "aaaaaaaaaaaaaayl",
                "aaaaaaaaaaaaaaym", "aaaaaaaaaaaaaayn", "aaaaaaaaaaaaaayo",
                "aaaaaaaaaaaaaayp", "aaaaaaaaaaaaaayq", "aaaaaaaaaaaaaayr",
                "aaaaaaaaaaaaaays", "aaaaaaaaaaaaaayt", "aaaaaaaaaaaaaayu",
                "aaaaaaaaaaaaaayv", "aaaaaaaaaaaaaayw", "aaaaaaaaaaaaaayx",
                "aaaaaaaaaaaaaayy", "aaaaaaaaaaaaaayz", "aaaaaaaaaaaaaaza",
                "aaaaaaaaaaaaaazb", "aaaaaaaaaaaaaazc", "aaaaaaaaaaaaaazd",
                "aaaaaaaaaaaaaaze", "aaaaaaaaaaaaaazf", "aaaaaaaaaaaaaazg",
                "aaaaaaaaaaaaaazh", "aaaaaaaaaaaaaazi", "aaaaaaaaaaaaaazj",
                "aaaaaaaaaaaaaazk", "aaaaaaaaaaaaaazl", "aaaaaaaaaaaaaazm",
                "aaaaaaaaaaaaaazn", "aaaaaaaaaaaaaazo", "aaaaaaaaaaaaaazp",
                "aaaaaaaaaaaaaazq", "aaaaaaaaaaaaaazr", "aaaaaaaaaaaaaazs",
                "aaaaaaaaaaaaaazt", "aaaaaaaaaaaaaazu", "aaaaaaaaaaaaaazv",
                "aaaaaaaaaaaaaazw", "aaaaaaaaaaaaaazx", "aaaaaaaaaaaaaazy",
                "aaaaaaaaaaaaaazz"
            ]) == [
                "aaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaab", "aaaaaaaaaaaaaaac",
                "aaaaaaaaaaaaaaad", "aaaaaaaaaaaaaaae", "aaaaaaaaaaaaaabc",
                "aaaaaaaaaaaaaabf", "aaaaaaaaaaaaaacb", "aaaaaaaaaaaaaacd",
                "aaaaaaaaaaaaaacg", "aaaaaaaaaaaaaadc", "aaaaaaaaaaaaaade",
                "aaaaaaaaaaaaaadh", "aaaaaaaaaaaaaaed", "aaaaaaaaaaaaaaei"
            ]


# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         class TrieNode:
#             def __init__(self) -> None:
#                 self.vals = [None] * (ord('z') - ord('a') + 1)
#                 self.end = False

#         class Trie:
#             def __init__(self):
#                 self.root = TrieNode()

#             def getIndex(self, char) -> int:
#                 return ord(char) - ord('a')

#             def addWord(self, word: str) -> None:
#                 cur = self.root
#                 for c in word:
#                     pos = self.getIndex(c)
#                     if cur.vals[pos] == None:
#                         newNode = TrieNode()
#                         cur.vals[pos] = newNode
#                         cur = newNode
#                     else:
#                         cur = cur.vals[pos]
#                 cur.end = True

#             def showWords(self) -> None:
#                 words = []

#                 def getWords(curNode: TrieNode, word: str) -> None:
#                     nonlocal words
#                     for i, node in enumerate(curNode.vals):
#                         if node != None:
#                             ch = ord('a') + i
#                             if node.end == True:
#                                 words.append(word + chr(ch))
#                             getWords(node, word + chr(ch))

#                 getWords(self.root, "")
#                 print(words)

#         trie = Trie()
#         for w in words:
#             trie.addWord(w)
#         #trie.showWords()

#         def dfs(node, word, i, j):
#             nonlocal board
#             nonlocal ans

#             if node.end:
#                 ans.add(word)

#             c = board[i][j]
#             board[i][j] = "_"

#             if i > 0:
#                 ch = board[i - 1][j]
#                 newNode = node.vals[ord(ch) - ord('a')]
#                 if newNode != None:
#                     dfs(newNode, word + ch, i - 1, j)
#             if i < len(board) - 1:
#                 ch = board[i + 1][j]
#                 newNode = node.vals[ord(ch) - ord('a')]
#                 if newNode != None:
#                     dfs(newNode, word + ch, i + 1, j)
#             if j > 0:
#                 ch = board[i][j - 1]
#                 newNode = node.vals[ord(ch) - ord('a')]
#                 if newNode != None:
#                     dfs(newNode, word + ch, i, j - 1)
#             if j < len(board[i]) - 1:
#                 ch = board[i][j + 1]
#                 newNode = node.vals[ord(ch) - ord('a')]
#                 if newNode != None:
#                     dfs(newNode, word + ch, i, j + 1)

#             board[i][j] = c

#         ans = set()
#         for i in range(len(board)):
#             for j in range(len(board[i])):
#                 dfs(trie.root, "", i, j)
#         print(board)
#         print(ans)
#         return sorted(list(ans))

#     def test(self):
#         assert self.findWords(board=[['o', 'a', 'a',
#                                       'n'], ['e', 't', 'a', 'e'],
#                                      ['i', 'h', 'k', 'r'],
#                                      ['i', 'f', 'l', 'v']],
#                               words=["oath", "pea", "eat",
#                                      "rain"]) == ["eat", "oath"]

if __name__ == "__main__":
    sol = Solution()
    sol.test()
    print((ord('_') - ord('a')))
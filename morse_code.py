"""International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes,
as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...",
"-","..-","...-",".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter.
For example, "cab" can be written as "-.-.-....-", (which is the concatenation "-.-." + "-..." + ".-").
We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation:
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".

Note:
The length of words will be at most 100.
Each words[i] will have length in range [1, 12].
words[i] will only consist of lowercase letters.
"""


class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        """
        morse_code_hash = dict(zip(
            tuple(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v',
                   'w', 'x', 'y', 'z']), tuple(
                [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---",
                 ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."])))
        """
        morse_code_hash = dict(a=".-", b="-...", c="-.-.", d="-..", e=".", f="..-.", g="--.", h="....", i="..",
                                   j=".---", k="-.-", l=".-..", m="--", n="-.", o="---", p=".--.", q="--.-", r=".-.",
                                   s="...", t="-", u="..-", v="...-", w=".--", x="-..-", y="-.--", z="--..")

        if len(words) > 100:
            return "List of words is too long, maximum list size should be 100"
        transform_list = []
        for word in words:
            if 1 > len(word) > 12:
                return "Each word should have length in range [1, 12]."
            transformed = ""
            for c in word:
                transformed += morse_code_hash[c]
            transform_list.append(transformed)
        print transform_list
        return len(set(transform_list))


sol = Solution()
words = ["gin", "zen", "gig", "msg"]
print(sol.uniqueMorseRepresentations(words))

class Solution:
    # O(n) time | O(1) space - where n is the length of the input list
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails = set()
        
        for email in emails:
            localName = email.split('@')[0]
            domainName = email.split('@')[1]
        
            if '+' in localName:
                plusPosition = localName.index('+')
                localName = localName[0:plusPosition]
                
            localName = localName.replace('.', '')
            newName = localName + '@' + domainName
            uniqueEmails.add(newName)
            
        return len(uniqueEmails)
    
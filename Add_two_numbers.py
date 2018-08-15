"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tenth = 10
        p, pp = l1, l2
        len, len2 = 0, 0

    
        #Calculate the longth of each node list
        while p or pp:
            if p:
                len+=1
                p = p.next
            
            if pp:
                len2+=1
                pp = pp.next

        
        #Calculate the Sum for both nodelist
        sum, sum2, sum_total = 0, 0, 0
        for i in range(len):
            sum+=l1.val*(10**i)
            l1=l1.next
         
          
        for a in range(len2):
            sum2+=l2.val*(10**a)
            l2=l2.next

        sum_total= sum+sum2
        
        #create l3           
        l3=list(map(int, list(str(sum_total))[::-1] ))
        return(l3)
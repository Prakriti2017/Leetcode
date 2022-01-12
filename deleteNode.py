class Solution:
    def delete_node(head,key):
        prev=None
        current=head
        while(current!=None):
            if(current==key):
                if(current==head):
                    head=head.next
                    current=head
                else:
                    prev.next=current.next
                    current=current.next
            else:
                prev=current
                current=current.next
        if(current==None):
            return head

        return head

So=Solution()
list_head = [0,1,2,3,4,5,6,7,8,9,10]
assert So.delete_node(list_head,3)==[0,1,2,4,5,6,7,8,910]


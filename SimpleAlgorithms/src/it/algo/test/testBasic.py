'''
Created on 10 mag 2017

@author: Enrico
'''
import unittest
from it.algo.linkedlist import remove_duplicates

# A A B C D C F G

rm = remove_duplicates

a1 = rm.Node("A")
a2 = rm.Node("A")
b = rm.Node("B")
c1 = rm.Node("C")
d = rm.Node("D")
c2 = rm.Node("C")
f = rm.Node("F")
g = rm.Node("G")
a3 = rm.Node("A")
b1 = rm.Node("B")
b2 = rm.Node("B")


a1.next = a2
a2.next = a3
a3.next = b
b.next = b1
b1.next = b2
b2.next = c1
c1.next = d
d.next = c2
c2.next = f
f.next = g

rm.aa1=a1

print ("Lista originale:")
rm.printLinkedList(a1)
print ("Lista copia:")
rm.printLinkedList(rm.aa1)
rm.removeDups(a1)
print ("-------------------------------------------------")
print ("Lista originale senza i doppioni:")
rm.printLinkedList(a1)
print ("Lista copia senza i doppioni (la lista copia fa riferimento all'oggetto lista originale)")
rm.printLinkedList(rm.aa1)


class Test(unittest.TestCase):

    
    def testName(self):
        #self.assertIn(str(rm.a1.next), "Z")
        #self.assertIn(str(rm.a1.val), "A")
        self.assertEquals(rm.a1.val, rm.aa1.val)
        

if __name__ == "__main__":
    
    unittest.main()

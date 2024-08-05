#include <stdio.h>

int main() {
    /*function call的時候怎麼去運作的
    1.會先更新cpu register, program counter或RIP
    2.從sp(stack pointer)來說的話
    如果是x64, rbp rsp會更新

     push ebp to the stack for a ebp backup. Then move esp to ebp. Now we can "play" with esp. 
     Before function returns, move back ebp to esp to restore what esp was before we moved esp to ebp. 
     Then pop ebp to restore ebp from the top of the stack.
    */
    return 0;
}
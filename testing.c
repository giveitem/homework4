#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    int child_pid = fork();
    if (child_pid != 0)
    {
        // parent process
        printf("Parent process");
    }
    else
    {
        // child process
        int grandchild_pid = fork();
        if (grandchild_pid != 0)
        {
            // grandchild process
            printf("Child process");
        }
        else
        {
            // parent process
            printf("Grandchild process");
            int greatgrandchild_pid = fork();
        }
    }

    return 0;
}

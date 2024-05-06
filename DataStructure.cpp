#include <iostream>
#include "./Stack/Stack.h"
#include "./Queue/Queue.h"
#include "./CircularQueue/CircularQueue.h"

using namespace std;

int main()
{
	CircularQueue circularQueue;
	circularQueue.Enqueue(1);
	circularQueue.Enqueue(2);
	circularQueue.Enqueue(3);
	circularQueue.Dequeue();
	circularQueue.Dequeue();
	circularQueue.Dequeue();
	circularQueue.Dequeue();
	circularQueue.Print();
}


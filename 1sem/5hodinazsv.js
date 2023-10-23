// function scope(){
//     const inside = "I am in function";
//     console.log(inside + " - first console log");
//     console.log(outside + " - first console log for outside");
//   }
//   const outside = "I am global";
//   scope();
  
  
//   console.log(outside + " - second console log");
  
//   console.log(inside + " - third console log");


function bubbleSort(arr)
{
    n = arr.length;
    let i, j, temp;
    let swapped;
    for (i = 0; i < n - 1; i++) 
    {
        swapped = false;
        for (j = 0; j < n - i - 1; j++) 
        {
            if (arr[j] > arr[j + 1]) 
            {
                // Swap arr[j] and arr[j+1]
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swapped = true;
            }
        }
        if (swapped == false)
        break;
    }
}

function printArray(arr, size)
{
  var i;
  for (i = 0; i < size; i++)
      console.log(arr[i] + " ");
}

var arr = [ 64, 34, 25, 12, 22, 11, 90 ];
var n = arr.length;
bubbleSort(arr);
console.log("Sorted array: ");
printArray(arr, n);
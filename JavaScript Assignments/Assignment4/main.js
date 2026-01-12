let array=[10,54,14,89,75,35,31,94,69,87];
function large_smallest_avg_in_array(array){
    let sum=0;
    for(let n of array){
        sum+=n;
    }
    console.log("Average of Elements from array :",sum/array.length);
    console.log("Largest Element in array :",Math.max(...array));
    console.log("Smallest Element in array :",Math.min(...array));
}

console.log(large_smallest_avg_in_array(array));
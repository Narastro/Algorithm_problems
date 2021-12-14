const binarySearch = (arr, target) => {
  if (!arr) return 0;
  arr.sort((a, b) => a - b);
  let start = 0;
  let end = arr.length - 1;
  while (start < end) {
    let mid = Math.floor((end + start) / 2);
    if (arr[mid] >= target) end = mid;
    else start = mid + 1;
  }
  return arr.length - start;
};

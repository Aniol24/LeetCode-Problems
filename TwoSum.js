


console.log(twoSum([3,3], 6));

function twoSum(nums, target){

    const ht = {};

    for (let i = 0; i < nums.length; i++){

        if(ht[target - nums[i]] !== undefined){
            return [ht[target - nums[i]], i];
        }else{
            ht[nums[i]] = i;
        }

    }
    return "error";

}
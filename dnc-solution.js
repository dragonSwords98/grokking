// Divide and Conquer Algorithm

// List/Array of True False tests where the first fail test will be marked as True, then all subsequent test will be True as well.
// Find the first failed test. (First True)

// Your api can call 5 selections as once, anywhere on the array.


// Divide and Conquer can be O(n/5) compared to O(n)/Average(log n) from BST of one selection search.


function requestOne(location) {
    return [true]
}

function requestFive(locations) {
    return [true]
}

/**
 * 
 * @param {*} spots 
 * @returns [bool, bool, bool, bool, bool]
 */
function performAPISearch(spots) {
    return request(spots)
}

function retrieveWindow(n, i) {
    if (!n.length % 2) {
        // even if window not at edge of list yet
        if (n.length - 1 >= i + 2) {
            return [-1, 0, 1, 2]
        }
    }

    // odd if all cases OR even if window is not at edge of list yet
    if (n.length - 1 >= i + 1) {
        return [-1, 0, 1]
    } else if (n.length - 1 >= i) {
        return [-1, 0]
    } else {
        return [-1]
    }
}

function isFirstFailedTestNoDivide(n, i) {
    w = retrieveWindow(n, i)
    foundATrue = false
    foundIndex = i
    while (w.length > 0) {
        examine = w.pop()
        if (requestOne(n[i + examine])) {
            if (foundATrue) {
                // you've already seen a True, here's another one to its left
                foundIndex = i + examine
            } else {
                // first True found! but where in the array is it?
                foundATrue = true
                foundIndex = i + examine
            }
        }
    }
    if (foundATrue) {
        // This is the left-most True found
        return foundIndex
    } else {
        // There were no Trues found
        return -1
    }
}



// HOW TO DIVIDE

// 1) Split array into five parts, and work 5 recursive operations (not true DNC)
// 2) Identify the window you need to check (size 3 or size 4) - lets assume the window is 1. always
//    - then instead, recurse the operation of searching 5 within 5 within 5. 


function Divide(start, end) {
    diff = end-start
    arr = []
    if (diff >= 5) {
        arr = [start, Math.floor(start + diff*1/5), Math.floor(start + diff*2/5), Math.floor(start + diff*3/5), Math.floor(start + diff*4/5), end]
    }
    else if (start <= end) {
        // Theres less than 5 elements remaining

        arr = []
        while (start < end) {
            arr.push(start)
            start = start + 1
        }
        while (arr.length < 5) {
            // it is legal to pad same indices as long as they are equal to the start index. this will resolve harmlessly as indices are tracked
            arr.push(end)
        }
    }
    return arr
}

function PadResults(parts, result) {
    return parts.map(p => result[p])
}

function DivideNConquer(start, end) {
    // counts all up to and including end
}

function FindFirstFailedTestDivide(result, start, end) {

    parts = Divide(start, end)
    paddedResult = PadResults(parts, result)
    // result = requestFive(parts)

    // Combine
    foundATrue = false
    foundFalseToLeftOfTrue = false
    foundIndex = -1
    foundFalseToLeftOfTrueIndex = -1
    while (parts.length > 0) {
        i = parts.pop()
        test = paddedResult.pop()
        if (test) {
            // Index of the leftmost failed test, found so far...
            foundIndex = i
            if (!foundATrue) {
                // First failed test found so far...
                foundATrue = true
            }
        } else if (foundATrue && !foundFalseToLeftOfTrue) {
            foundFalseToLeftOfTrue = true
            foundFalseToLeftOfTrueIndex = i
        }
    }
    if (foundATrue) {
        // We know the failed test is in front foundIndex and to the right of foundFalseToLeftOfTrueIndex

        if (foundFalseToLeftOfTrueIndex + 1 === foundIndex || foundFalseToLeftOfTrueIndex === foundIndex) {
            return foundIndex
        }

        return FindFirstFailedTestDivide(result, foundFalseToLeftOfTrueIndex, foundIndex)
    } else {
        return -1
    }
    // }

    // dnc = []
    
    // dnc[0] = DivideNConquer(parts[0], parts[1])
    // dnc[1] = DivideNConquer(parts[1]+1, parts[2])
    // dnc[2] = DivideNConquer(parts[2]+1, parts[3])
    // dnc[3] = DivideNConquer(parts[3]+1, parts[4])
    // dnc[4] = DivideNConquer(parts[4]+1, parts[5])

    // return Combine(dnc)
}


function testAll(name, n, answer) {
    // console.log(`Testing: ${name}`)
    check = FindFirstFailedTestDivide(n, 0, n.length - 1)
    
    // if (check === -1) {
    //     console.log('All tests passed!')
    // } else {
    //     console.log(`Test failed at ${check}`)
    // }
    
    if (answer !== check) {
        console.log(`Testing: ${name}`)
        console.error(`INCORRECT! Should be ${answer}, was ${check} in ${n}`)
    // } else {
        // console.log(`Was ${check} in ${n}`)
    }
}

function randomTestGenerator(arraySize) {
    falses = Math.floor(Math.random() * arraySize)
    if (!arraySize) {
        return [[], -1]
    }
    return [
        [
            ...Array.from({length: falses}, () => false),
            ...Array.from({length: arraySize - falses}, () => true)
        ],
        falses
    ]
}

// TESTFIVE1 = [false,false,false,false,false]
// testAll('TESTFIVE1', TESTFIVE1, -1)
// TESTFIVE2 = [false,false,true,true,true]
// testAll('TESTFIVE2', TESTFIVE2, 2)
// TESTFIVE3 = [true,true,true,true,true]
// testAll('TESTFIVE3', TESTFIVE3, 0)
// TESTFIVE4 = [false,true,true,true,true]
// testAll('TESTFIVE4', TESTFIVE4, 1)
// TESTFIVE5 = [false,false,false,true,true]
// testAll('TESTFIVE5', TESTFIVE5, 3)
// TESTFIVE6 = [false,false,false,false,true]
// testAll('TESTFIVE6', TESTFIVE6, 4)
// TESTFIVE7 = [false,false,false,false,false,false]
// testAll('TESTFIVE7', TESTFIVE7, -1)
// TESTFIVE8 = [false,false,false,false]
// testAll('TESTFIVE8', TESTFIVE8, -1)
// TESTFIVE9 = [false,false,false]
// testAll('TESTFIVE9', TESTFIVE9, -1)
// TESTFIVE10 = [false,false]
// testAll('TESTFIVE10', TESTFIVE10, -1)
// TESTFIVE11 = [false]
// testAll('TESTFIVE11', TESTFIVE11, -1)
// TESTFIVE12 = [true]
// testAll('TESTFIVE12', TESTFIVE12, 0)
TESTFIVE13 = []
testAll('TESTFIVE13', TESTFIVE13, -1)
// TESTFIVE14 = [true, true, true]
// testAll('TESTFIVE14', TESTFIVE14, 0)
// TESTFIVE15 = [true, true]
// testAll('TESTFIVE15', TESTFIVE15, 0)
// TESTFIVE16 = [true, true, true, true]
// testAll('TESTFIVE16', TESTFIVE16, 0)
// TESTFIVE17 = [true, true, true, true, true, true]
// testAll('TESTFIVE17', TESTFIVE17, 0)
// TESTFIVE18 = [true, true, true, true, true, true, true]
// testAll('TESTFIVE18', TESTFIVE18, 0)
// TESTFIVE19 = [false, true, true, true, true, true, true]
// testAll('TESTFIVE19', TESTFIVE19, 1)
// TESTFIVE20 = [false, false, false, true, true, true, true]
// testAll('TESTFIVE20', TESTFIVE20, 3)
// TESTFIVE21 = [false, false, true, true, true, true, true]
// testAll('TESTFIVE21', TESTFIVE21, 2)
// TESTFIVE22 = [false,false,false,false,false,false,false,false,false,true]
// testAll('TESTFIVE22', TESTFIVE22, 9)


doRandomTests = 0
NUMBEROFTESTS = 5000
ARRAYSIZERANGE = 5000
testsConducted = 1
while (doRandomTests < NUMBEROFTESTS) {
    size = Math.floor(Math.random() * ARRAYSIZERANGE)
    testAll(`Random Test #${doRandomTests}`, ...randomTestGenerator(size))
    doRandomTests = doRandomTests + 1
    testsConducted = testsConducted + 1
}

console.log(`Total tests conducted: ${testsConducted}`)

















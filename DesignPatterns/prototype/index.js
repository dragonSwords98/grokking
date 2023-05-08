
const getRandomIntBelowNum = (max) => {
    return Math.floor(Math.random()* max)
}

const dog = {
    tricks: ['heel', 'agility', 'sit', 'down', 'stay', 'speak', 'roll', 'play dead'],
    setTricks(tricks) {
        this.tricks = tricks
    },
    doATrick() {
        if (this.tricks.length > 0)
            return this.tricks[getRandomIntBelowNum(this.tricks.length)]
        else
            return NaN
    },
}

// This allows one use prototypical inheritance, built-in to JS's capabilities
const journey = Object.create(dog, { name: { value: 'Journey'} })

console.log(journey)
console.log(journey.doATrick())


// Footnotes: I removed typescript syntax so that Node.js will just run it without a transpile
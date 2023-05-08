// # Contributed by: Bryan Ling

class Noodles {
    noodles: string;
    soupBase: string;
    dry: boolean = true;
    vegetarian: boolean = true;
    bowlSize: number;
    temperature: number;
    spicy: number;
    proteins: string[];

    // constructor(
    //     public noodleType: string,
    //     public soupBase: string,
    //     public bowlSize: number,
    //     public temperature: number,
    //     public spicy: boolean,
    //     public vegan: boolean,
    //     public proteins: string[]
    // ) {}
    constructor(public name: string) {}

    addNoodle(noodles: string) {
        this.noodles = noodles;
        return this
    }
    addSoupBase(soupBase: string, containsMeat: boolean) {
        this.soupBase = soupBase;
        this.dry = false;
        if (containsMeat) this.vegetarian = false
        return this
    }
    addBowlSize(bowlSize: number) {
        this.bowlSize = bowlSize;
        return this
    }
    heatToTemperature(temperature: number) {
        this.temperature = temperature;
        return this
    }
    addSpicynessLevel(spicy: number) {
        this.spicy = Math.max(this.spicy, spicy)
        return this
    }
    addProtein(protein: string, isMeat: boolean) {
        this.proteins.push(protein)
        if (isMeat) this.vegetarian = false
        return this
    }
    getName() { return this.name }
    isItVegetarian() { return this.vegetarian }
    isDry() { return this.dry}
}

const makeMySomeNoodles = new Noodles('')

makeMySomeNoodles
    .addBowlSize(5)
    .addNoodle('Udon')
    .addProtein('Tofu', true)

console.log(makeMySomeNoodles.isItVegetarian())
console.log(makeMySomeNoodles.isDry())

makeMySomeNoodles
    .addProtein('Fish', true)
    .addProtein('Beef', true)
    .addSoupBase('All Vegetable Broth', false)

console.log(makeMySomeNoodles.isItVegetarian())

makeMySomeNoodles.heatToTemperature(30)


// this was commonly seen in JQuery, but its out of style

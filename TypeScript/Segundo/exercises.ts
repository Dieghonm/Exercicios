class Person {
  name: string;
  birthDate: Date;
  age: number;

  constructor(name: string, birthDate: Date, age: number;) {
      this.name  = name;
      this.birthDate  = birthDate;
      this.age  = age;
  }

  speak(): void {
      console.log(`${this.name} está falando.`);
  }

  eat(): void {
      console.log(`${this.name} está comendo.`)
  }

  walk(): void {
      console.log(`${this.name} está andando.`)
  }
}

// bad
function canDrink(person) {
  if (person?.age != null) {
  }
  if (person.age < 18) {
    console.log("Nope");
  } else if (person.age < 21) {
    console.log("Not in the US");
  } else {
    console.log("Yes you can");
  }
  {
    console.log("You are not a person");
  }
}

// better: early return
function canDrinkBetter(person) {
  if (person?.age != null) {
    console.log("You are not a person");
    return;
  }

  if (person.age < 18) {
    console.log("Nope");
  }

  if (person.age < 21) {
    console.log("Not in the US");
  }

  console.log("Yes");
}

// better2: result variable
function canDrinkBetter2(person) {
  if (person?.age != null) {
    console.log("You are not a person");
    return;
  }

  let result = "Yes";
  if (person.age < 18) {
    result = "Nope";
  }

  if (person.age < 21) {
    result = "Not in the US";
  }

  console.log(result);
}

// best: use another function
function canDrinkBetter2(person) {
  if (person?.age != null) {
    console.log("You are not a person");
    return;
  }

  let result = canDrinkResponse(person.age);
  console.log(result);
}

function canDrinkResponse(age) {
  if (age < 18) return "Nope";
  if (age < 21) return "Not in the US";
  return "Yes";
}

const fs = require("fs");
const inputPath = "a.in", outputPath = "a2.out";
const thresh = 7;
let horizontals = [], verticals = [];

fs.readFileSync(inputPath, 'utf-8').split('\n').forEach((im, i) => {
    let args = im.split(' ');
    let photo = {};
    photo.id = i;
    photo.orientation = args[0];
    photo.tags = args.slice(2, args.length);

    if (photo.orientation === 'H') horizontals.push(photo);
    else verticals.push(photo);
})

fs.writeFileSync(outputPath, horizontals.length + verticals.length / 2 + "\n");

// Pair verticals
for (let i = 0; i < verticals.length - 1; i++) {
    for (let j = i + 1; j < verticals.length; j++) {
        let inters = verticals[i].tags.filter(value => verticals[j].tags.includes(value));
        if (inters.length === 0) {
            horizontals.push({ id: verticals[i].id + " " + verticals[j].id, orientation: 'H', tags: verticals[i].tags.concat(verticals[j].tags) });
            verticals.splice(i, 1);
            verticals.splice(j - 1, 1);
            i--;
            break;
        }
    }
}

for (let i = 0; i < verticals.length - 1; i += 2) {
    horizontals.push({ id: verticals[i].id + " " + verticals[i + 1].id, orientation: 'H', tags: verticals[i].tags.concat(verticals[i + 1].tags) });
}

let sol = '';
let flag = false;
for (let i = 0; i < horizontals.length - 1; i++) {
    let photo = null, index2 = -1;

    for (let j = i + 1; j < horizontals.length; j++) {
        let out1 = horizontals[i].tags.filter(value => horizontals[j].tags.includes(value)).length;
        let out2 = horizontals[i].tags.length - out1;
        let out3 = horizontals[j].tags.length - out1;

        let score = Math.min(out1, out2, out3);
        if (score >= thresh) {
            photo = horizontals[j];
            index2 = j;
            flag = true;
            break;
        }
    }

    if(!flag) photo = horizontals.pop();

    sol += (horizontals[i].id + "\n" + photo.id + "\n");

    if(flag){
        horizontals.splice(i, 1);
        horizontals.splice(index2 - 1, 1); i--;
        flag = false;
    }
    else{
        horizontals.splice(i, 1);
        i--;
    }
}

fs.appendFileSync(outputPath, sol);

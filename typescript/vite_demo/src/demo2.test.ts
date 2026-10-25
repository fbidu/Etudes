import { beforeEach, expect, it } from "vitest";

let data: Record<string, string>;
let data2: number[];

beforeEach(() => {
    data = { "name": "Felipe" };
    data2 = [1, 2, 3];
});

it("has name", () => {
    expect(data).toHaveProperty("name");
})

it("has 3 items", () => {
    expect(data2.length).toEqual(3);
})
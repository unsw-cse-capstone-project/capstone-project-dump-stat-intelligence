# API Spec

## Users

### Login User

POST `/user/login`

```
{
  user: {
    email,
    password
  }
}
```

#### Expected Response


### Register User

POST `/user/register`

```
{
  user: {
    name,
    email,
    password
  }
}
```

---

## Cookbook

### Get User Cookbook
(Authorization with token)
GET `/user/cookbook`

**Query String**
`?limit=10&offset=21`

- limit: number of recipes to respond with
- offset: offset by n recipes (calculated as page * limit)


#### Expected Response

### Add to User Cookbook
(Authorization with token)
POST `/user/cookbook`

```
{
  recipeId: id
}
```

#### Expected Response

### Delete from User Cookbook
(Authorization with token)
DELETE `/user/cookbook/{id}`

#### Expected Response

---

## Pantry

### Get User Pantry
(Authorization with token)
GET `/user/pantry`

**Query String**
`?limit=10&offset=21`

- limit: number of recipes to respond with
- offset: offset by n recipes (calculated as page * limit)


#### Expected Response

### Add to User Pantry
(Authorization with token)
POST `/user/pantry`

```
{
  ingredient: {ingredient Object}
}
```

#### Expected Response

### Delete from User Pantry
(Authorization with token)
DELETE `/user/pantry/{id}`

#### Expected Response

---

## Recipes

### All Recipes
GET `/recipes`

**Query String**
`?meal={dinner}&diet={vegan}&limit={10}&offset={21}`

- limit: number of recipes to respond with
- offset: offset by n recipes (calculated as page * limit)
- meal: mealType string
- diet: dietry requirement string

#### Expected Response

- more: boolean if there are more pages of recipes

### Get Recipe
GET `/recipes/{id}`

#### Expected Response

### Create Recipe
(Authorization with token)
POST `/recipes`

```
{
  recipe: {recipe object}
}
```

### Update Recipe
(Authorization with token)
PUT `/recipes/{id}`

```
{
  recipe: {recipe object}
}
```

#### Expected Response

### Delete Recipe
(Authorization with token)
DELETE `/recipes/{id}`

#### Expected Response

---

## Ingredients

### Search for ingredients
GET `/ingredients`

**Query String**
`?search={name}&limit={10}&offset={21}`

- search: name of ingredient to fuzzy match
- limit: number of recipes to respond with
- offset: offset by n recipes (calculated as page * limit)

#### Expected Response

### Get an ingredient
GET `/ingredients/{id}`


### Create an ingredient
POST `/ingredients`

TBD: are ingredients associated with users?
Who can edit and delete?

```
{
  ingredient: {ingredient Object}
}
```
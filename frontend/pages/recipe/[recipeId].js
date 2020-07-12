import Head from "next/head";
import { useRouter } from "next/router";
import React, { useState, useEffect } from "react";
import Link from "next/link";

import RecipeAPI from "../../lib/api/recipe";
import Error from "../../components/Error/Error";

import { useDispatch, useSelector } from "react-redux";
import {
  add_favourite,
  remove_favourite,
} from "../../lib/redux/actions/authAction";
import { load_create } from "../../lib/redux/actions/createAction";
import { recipes_update } from "../../lib/redux/actions/recipesAction";

const Recipe = (props) => {
  const dispatch = useDispatch();
  let isLoggedIn = useSelector((state) => state.auth.isLoggedIn);
  const uid = useSelector((state) => state.auth.uid);
  const router = useRouter();

  let [recipe, setRecipe] = useState(null);
  const recipes = useSelector((state) => state.recipes.recipes);

  const [deleteLoading, setDeleteLoading] = useState(false);

  useEffect(() => {
    let recipeId = window.location.href.split("/").pop();
    if (recipes.length == 0) {
      // load the recipes
      dispatch(recipes_update());
    }
    setRecipe(recipes.filter((r) => r.id == recipeId)[0]);
  });

  const [error, setError] = useState(null);

  const handleDelete = async (e) => {
    setDeleteLoading(true);
    const res = await RecipeAPI.delete(recipe.id);
    router.push("/explore");
    setDeleteLoading(false);
  };

  if (error) {
    return <Error message={error.statusText} />;
  }

  if (recipe == null) {
    return <p>Loading</p>;
  }

  function addFave() {
    dispatch(add_favourite({ title: recipe.name, src: null, id: recipe.id }));
    setRecipe({
      ...recipe,
      isFavourite: true,
    });
  }

  function removeFave() {
    dispatch(remove_favourite(recipe.id));
    setRecipe({
      ...recipe,
      isFavourite: false,
    });
  }

  let faveButton = null;
  let controlButtons = null;
  console.log("isloggedin", isLoggedIn);
  console.log("uid", uid);
  console.log("recipe id", recipe.author.id);
  if (isLoggedIn && uid === recipe.author.id) {
    controlButtons = (
      <>
        <Link href="/recipe/create">
          <a
            onClick={() => dispatch(load_create(recipe.id))}
            className="button is-light"
          >
            Edit
          </a>
        </Link>
        <a
          className={`button is-light is-danger ${
            deleteLoading ? "is-loading" : null
          }`}
          onClick={handleDelete}
        >
          Delete
        </a>
      </>
    );
  } else if (isLoggedIn) {
    faveButton = recipe.isFavourite ? (
      <a onClick={removeFave} className="button is-light is-warning">
        UnFavourite
      </a>
    ) : (
      <a onClick={addFave} className="button is-light is-warning">
        Favourite
      </a>
    );
  }

  return (
    <div>
      <Head>
        <title>Pantry Pirate | Create</title>
      </Head>
      <div className="container">
        <div className="columns is-centered">
          <div className="box column is-10">
            <div className="columns">
              <div className="column is-4">
                <h1 className="title is-2">{recipe.name}</h1>
                <p>
                  Author: {recipe.author.username} | Cook time:{" "}
                  {recipe.cook_time}
                </p>
                <div className="tags">
                  {recipe.diet_req.map((diet, idx) => (
                    <span className="tag" key={idx}>
                      {diet.name}
                    </span>
                  ))}
                </div>
                <div className="buttons">
                  {faveButton}
                  {controlButtons}
                </div>
              </div>
              <div className="column is-8">
                <img
                  src={`https://source.unsplash.com/1200x600/?${recipe.name}`}
                />
              </div>
            </div>

            <hr />
            <div className="columns">
              <div className="column is-4">
                <h4 className="title is-4">Ingredients</h4>
                <ul>
                  {recipe.ingredients.map((ingredient, idx) => (
                    <li key={idx}>
                      {ingredient.amount} {ingredient.unit}{" "}
                      {ingredient.ingredient.name}
                    </li>
                  ))}
                </ul>
              </div>
              <div className="column is-6">
                <h4 className="title is-4">Method</h4>
                <p style={{ whiteSpace: "pre-wrap" }}>{recipe.method}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Recipe;

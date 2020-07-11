import Head from "next/head";
import { useRouter } from "next/router";
import React, { useState, useEffect } from "react";

import RecipeAPI from "../../lib/api/recipe";
import Error from "../../components/Error/Error";

import { useDispatch, useSelector } from "react-redux";
import { add_favourite, remove_favourite } from "../../lib/redux/actions/authAction";

const Recipe = (props) => {
  const dispatch = useDispatch();
  let isLoggedIn = useSelector(state => state.auth.isLoggedIn)
  const router = useRouter();
  const [loading, setLoading] = useState(false);
  const [deleteLoading, setDeleteLoading] = useState(false);
  const [recipe, setRecipe] = useState({
    id : null,
    name: "",
    cook_time: "",
    method: "",
    author: { name: "" },
    isAuthor : false,
    isFavourite : false,
    diet_req: [],
    meal_cat: [],
    ingredients: [],
  });
  const [error, setError] = useState(null);

  useEffect(() => {
    // don't know why but router.query is not returning the id?
    let recipeId = window.location.href.split("/").pop();
    RecipeAPI.get(recipeId).then(
      ({ data }) => {
        console.log(data);
        setRecipe(data);
        setLoading(false);
      },
      (err) => {
        setError(err.response);
        setLoading(false);
      }
    );
  }, []);

  const handleDelete = async (e) => {
    setDeleteLoading(true);
    const res = await RecipeAPI.delete(recipe.id, ""); // TODO: token authentication
    console.log(res);
    router.push("/explore");
    setDeleteLoading(false);
  };
  
  if (error) {
    return <Error message={error.statusText} />;
  }

  if (loading) {
    return <p>Loading</p>;
  }

  function addFave() {
    dispatch(add_favourite({title : recipe.name, src : null,  id : recipe.id}))
    setRecipe({
      ...recipe,
      isFavourite : true
    })
  }

  function removeFave() {
    dispatch(remove_favourite(recipe.id));
    setRecipe({
      ...recipe,
      isFavourite : false
    })
  }


  let faveButton = null;
  if (isLoggedIn) {
    faveButton = recipe.isFavourite ? <a onClick={removeFave} className="button is-light is-warning">UnFavourite</a> : <a onClick={addFave} className="button is-light is-warning">Favourite</a>
  }
  let controlButtons = null;
  if (recipe.isAuthor) {
    controlButtons = <> 
      <a className="button is-light">Edit</a>
      <a className={`button is-light is-danger ${deleteLoading ? "is-loading" : null}`} onClick={handleDelete}>Delete</a>
    </>
  }

  return (
    <div>
      <Head>
        <title>Pantry Pirate | Create</title>
      </Head>
      <div className="container">
        <div className="columns is-centered">
          <div className="box column is-10">
            <h1 className="title is-2">{recipe.name}</h1>
            <img src={`https://source.unsplash.com/1200x600/?${recipe.name}`} />
            <p>
              Author: {recipe.author.username} | Cook time: {recipe.cook_time}
            </p>
            <div className="tags">
              {recipe.diet_req.map((diet, idx) => (
                <span className="tag" key={idx}>
                  {diet.name}
                </span>
              ))}
            </div>
            <div className="buttons">
              
              { faveButton }
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
                <p>{recipe.method}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Recipe;


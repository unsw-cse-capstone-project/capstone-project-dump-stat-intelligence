import styles from "./Edit.module.scss";
import { useState, useEffect } from 'react';
import { useSelector, useDispatch } from "react-redux";
import {
  clear_create,
  save_create,
  update_recipe,
} from "../../lib/redux/actions/createAction";
import { useRouter } from "next/router";
import NewIngredient from "./NewIngredient";
import RecipeAPI from "../../lib/api/recipe";

export default function Preview() {
  const dispatch = useDispatch();
  const router = useRouter();
    const [ingredients, setIngredients] = useState([
      "coriander", "chicken"
  ]);


  
  let creation = useSelector((state) => state.create);
  let user = useSelector((state) => state.auth.userInfo);
  

  const discard = () => {
    dispatch(clear_create());
    router.push("/cookbook");
  };

  const createRecipe = () => {
    if (isCompleteRecipe()) {
      dispatch(save_create());
      router.push("/cookbook");
      RecipeAPI.getAll(ingredients.join(","), "", "");
    } else {
      document.getElementById("createrror").classList.toggle("is-active");
    }
  };

  const updateRecipe = () => {
    if (isCompleteRecipe()) {
      dispatch(update_recipe());
      router.push("/cookbook");
    } else {
      document.getElementById("createrror").classList.toggle("is-active");
    }
  }


  function isCompleteRecipe() {
    if (creation.name === "" || creation.method === "" || creation.cook_time === "" 
    || creation.image_URL === "" 
    || creation.ingredients.length === 0 || creation.meal_cat.length === 0) return false;

    return true;
  }

  useEffect(() => {
    RecipeAPI.discover()
    .then(res => {
        let ings = res.data.search.split(",");
        for (let i = 0; i < ings.length; i++) {
            ings[i] = ings[i].split("|").join(" ")
        }
        setIngredients(ings)

    })
    .catch(err => console.log(err))
}, [])

  return (
    <div className="container">
      <div className="columns is-centered">
        <NewIngredient id="new-ingredient" />
        <div className="box column is-11">
          <div className="notification is-warning">
            <strong>Preview</strong> - Use the edit button below to start
            editing this recipe
          </div>
          {
            creation.suggest ? 
            <div className={styles.suggestion}>
              <div className={`${styles.choice} tags`}>
                  <span className="is-6">Need inspiration? Use these commonly searched ingredients - </span>
                  {
                      ingredients.map((val, idx) => (
                          <span key={idx} className="tag is-dark">
                              {val}
                          </span>
                      ))
                  }
              </div>
            </div>
            : ""
          }
          <h1 className="title is-2">{`${creation.name}`}</h1>
          <img
            style={{
              width: "100%",
              maxHeight: "500px",
              objectFit: "cover",
              display: "block",
            }}
            src={creation.image_URL}
          />
          <p>
            Author: {user.username} | Cook time: {creation.cook_time}
          </p>
          <div className="tags">
            {creation.diet_req.map((diet, idx) => (
              <span className="tag" key={idx}>
                {diet.name}
              </span>
            ))}
          </div>

          <hr />
          <div className="columns">
            <div className="column is-4">
              <h4 className="title is-4">Ingredients</h4>
              <ul>
                {creation.ingredients.map((ingredient, idx) => (
                  <li key={idx}>
                    {ingredient.amount} {ingredient.unit} {" "}
                    {ingredient.ingredient.name + ", " + ingredient.adjective}
                  </li>
                ))}
              </ul>
            </div>
            <div className="column is-6">
              <h4 className="title is-4">Method</h4>
              <p className={styles.wrap}>{creation.method}</p>
            </div>
          </div>
          <hr />
          <div className="buttons">
            {creation.id ? (
              <>
                <button
                  onClick={updateRecipe}
                  className="button is-light is-success"
                >
                  Save Changes
                </button>
                <button onClick={discard} className="button is-light is-danger">
                  Discard Changes
                </button>
              </>
            ) : (
              <>
                <button
                  onClick={createRecipe}
                  className="button is-light is-success"
                >
                  Add Recipe
                </button>
                <button onClick={discard} className="button is-light is-danger">
                  Discard
                </button>
              </>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

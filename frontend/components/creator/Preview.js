import styles from "./Edit.module.scss";

import { useSelector, useDispatch } from "react-redux";
import {
  clear_create,
  save_create,
} from "../../lib/redux/actions/createAction";
import { useRouter } from "next/router";
import NewIngredient from "./NewIngredient";

export default function Preview() {
  const dispatch = useDispatch();
  const router = useRouter();

  let creation = useSelector((state) => state.create);
  let user = useSelector((state) => state.auth.userInfo);

  const discard = () => {
    dispatch(clear_create());
    router.push("/cookbook");
  };

  const createRecipe = () => {
    dispatch(save_create());
  };

  return (
    <div className="container">
      <div className="columns is-centred">
        <NewIngredient id="new-ingredient" />
        <div className="box column is-10">
          <h1 className="title is-2">{`PREVIEW: ${creation.name}`}</h1>
          {creation.name !== "New Recipe" ? (
            <img
              src={`https://source.unsplash.com/1200x600/?${creation.name}`}
            />
          ) : (
            ""
          )}
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
                    {ingredient.amount} {ingredient.unit}{" "}
                    {ingredient.ingredient.name}
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
                  onClick={createRecipe}
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

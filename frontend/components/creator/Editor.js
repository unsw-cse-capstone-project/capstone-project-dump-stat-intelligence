import styles from "./Edit.module.scss";
import React, { useState } from "react";
import { useRouter } from "next/router";

import RecipeAPI from "../../lib/api/recipe";

export default function Editor() {
  const router = useRouter();
  const [active, setActive] = useState(0);
  const [isLoading, setIsLoading] = useState(false);
  const [recipe, setRecipe] = useState({
    name: "",
    author: "",
    cook_time: "",
    image_url: "",
    ingredients: [],
    diet_req: [],
    meal_cat: [],
    method: "",
  });

  const handleInput = ({ target }, field) => {
    setRecipe((prev) => ({ ...prev, [field]: target.value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    RecipeAPI.create(recipe, "")
      .then((res) => {
        console.log("getting this far!");
        router.push(`/recipe/${res.data.id}/`);
        setIsLoading(false);
      })
      .catch((err) => {
        console.error(err.response);
        setIsLoading(false);
      });
  };

  function chooseTab(num) {
    document
      .getElementById(`editBox${active}`)
      .classList.remove(styles.showBox);
    setActive(num);
    document.getElementById(`editBox${num}`).classList.add(styles.showBox);
  }
  return (
    <>
      <div id="editor" className={styles.editor}>
        <div className="tabs">
          <ul>
            <li
              onClick={() => chooseTab(0)}
              className={active === 0 ? "is-active" : ""}
            >
              <a>General</a>
            </li>
            <li
              onClick={() => chooseTab(1)}
              className={active === 1 ? "is-active" : ""}
            >
              <a>Ingredients</a>
            </li>
            <li
              onClick={() => chooseTab(2)}
              className={active === 2 ? "is-active" : ""}
            >
              <a>Method</a>
            </li>
          </ul>
        </div>
        <div id="editBox0" className={`${styles.editBox} ${styles.showBox}`}>
          <div className="form">
            <div className="field control">
              <label className="label">Title</label>
              <input
                name="title"
                className="input"
                type="text"
                value={recipe.name}
                onChange={(e) => handleInput(e, "name")}
              />
            </div>
            <div className="field control">
              <label className="label">Cook time</label>
              <input
                name="cook_time"
                className="input"
                type="text"
                value={recipe.cook_time}
                onChange={(e) => handleInput(e, "cook_time")}
              />
            </div>
            <div className="field control">
              <label className="label">
                Author ID (until auth is implemented)
              </label>
              <input
                name="author"
                className="input"
                type="text"
                value={recipe.author}
                onChange={(e) => handleInput(e, "author")}
              />
            </div>
            <div className="field control">
              <label className="label">Image URL</label>
              <input
                name="cook_time"
                className="input"
                type="text"
                value={recipe.image_url}
                onChange={(e) => handleInput(e, "image_url")}
              />
            </div>
            <button
              className={`button is-success is-light ${
                isLoading ? "is-loading" : null
              }`}
              onClick={handleSubmit}
            >
              Add Recipe
            </button>
          </div>
        </div>
        <div id="editBox1" className={styles.editBox}>
          List of current ingredients
          <br />
          Each one can be deleted or edited
          <br />
          Add ingredient form at bottom
          <br />
          How to redorder them??
        </div>
        <div id="editBox2" className={styles.editBox}>
          <div className="field control">
            <textarea
              className="textarea input"
              onChange={(e) => handleInput(e, "method")}
              value={recipe.method}
            ></textarea>
          </div>
        </div>
      </div>
    </>
  );
}

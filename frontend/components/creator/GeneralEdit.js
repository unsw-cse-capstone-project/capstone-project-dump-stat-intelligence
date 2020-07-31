import styles from "./Edit.module.scss";

import axios from "axios";

import { useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import {
  update_create,
  add_category,
  remove_category,
} from "../../lib/redux/actions/createAction";

import DropItem from "./DropItem";

export default function GeneralEdit() {
  const dispatch = useDispatch();
  let recipe = useSelector((state) => state.create);
  function handleInput(event) {
    dispatch(update_create(event.target.name, event.target.value));
  }

  let [unsplashImgs, setUnsplashImgs] = useState([]);

  const unsplashSearch = () => {
    const CLIENT_ID = "55PcQTaRixIN9faqVZzA3K3NwzMoAwqXiTr8GPurdB0";
    axios
      .get(
        `https://api.unsplash.com/search/photos/?query=${recipe.name}&orientation=squarish&client_id=${CLIENT_ID}`
      )
      .then((res) => {
        console.log(res);
        let urls = [];
        res.data.results.forEach((img) => {
          urls.push(img.urls.regular);
        });
        setUnsplashImgs(urls);
        // res.body.json();
      });
  };

  const setUnsplashImage = (url) => {
    dispatch(update_create("image_URL", url));
  };

  //Need to do some processing because data in backend is different
  let meal = {
    Breakfast: false,
    Lunch: false,
    Dinner: false,
    Snack: false,
    Dessert: false,
    Brunch: false,
  };
  let diet = {
    Vegan: false,
    Vegetarian: false,
    "Gluten-free": false,
    "Dairy-free": false,
  };
  recipe.meal_cat.map((cat) => {
    meal[cat.name] = true;
  });
  recipe.diet_req.map((dietar) => {
    diet[dietar.name] = true;
  });

  let images = (
    <div className="field">
      <div className="columns is-multiline">
        {unsplashImgs.map((url, idx) => (
          <div key={idx} className="column is-6">
            <img
              style={{
                width: "100%",
                height: "150px",
                objectFit: "cover",
                display: "block",
                cursor: "pointer",
              }}
              src={url}
              onClick={() => {
                setUnsplashImage(url);
              }}
            />
          </div>
        ))}
      </div>
    </div>
  );

  return (
    <div className="form">
      <div className="field control">
        <label className="label">Title</label>
        <input
          name="name"
          className="input"
          type="text"
          value={recipe.name}
          onChange={handleInput}
        />
      </div>
      <div className="field control">
        <label className="label">Cook time</label>
        <input
          name="cook_time"
          className="input"
          type="text"
          value={recipe.cook_time}
          onChange={handleInput}
        />
      </div>
      <hr />
      <div className="field" style={{ margin: "0.5rem 0" }}>
        <button style={{marginBottom:"2rem"}} className="button" onClick={() => unsplashSearch()}>
          Suggest some images...
        </button>
        {images}
      </div>
      <div className="field control">
        <label className="label">Image URL</label>
        <input
          name="image_URL"
          className="input"
          type="text"
          value={recipe.image_URL}
          onChange={handleInput}
        />
      </div>
      <hr />
      <div className="field control">
        <label className="label">Meal type</label>
        <div onFocus={e => {let obj = document.getElementById("dropdown-cat"); obj.classList.add(styles.show); obj.firstElementChild.focus();}} className="select dropdown" style={{ width: "100%" }}>
          <div style={{ width: "100%" }} className="dropdown-trigger">
            <button
              className="button"
              style={{ width: "100%" }}
              aria-haspopup="true"
              aria-controls="dropdown-cat"
            >
              <span>Meal type</span>
              <span className="icon is-small">
                <i className="fas fa-check" aria-hidden="true"></i>
              </span>
            </button>
          </div>
          <div
            style={{ width: "100%" }}
            className="dropdown-menu"
            id="dropdown-cat"
            role="menu"
          >
            <div tabIndex="0" className={`dropdown-content ${styles.stopBorder}`} onBlur={e => {document.getElementById("dropdown-cat").classList.remove(styles.show)}}>
              {Object.keys(meal).map((key, idx) => (
                <DropItem
                  key={idx}
                  name={key}
                  is_checked={meal[key]}
                  add={add_category}
                  remove={remove_category}
                  category="meal_cat"
                />
              ))}
            </div>
          </div>
        </div>
      </div>
      <div className="field control">
        <label className="label">Dietary requirements</label>
        <div onFocus={e => {let obj = document.getElementById("dropdown-diet"); obj.classList.add(styles.show); obj.firstElementChild.focus();}}  className="select dropdown" style={{ width: "100%" }}>
          <div style={{ width: "100%" }} className="dropdown-trigger">
            <button
              className="button"
              style={{ width: "100%" }}
              aria-haspopup="true"
              aria-controls="dropdown-diet"
            >
              <span>Dietary requirements</span>
              <span className="icon is-small">
                <i className="fas fa-check" aria-hidden="true"></i>
              </span>
            </button>
          </div>
          <div
            style={{ width: "100%" }}
            className="dropdown-menu"
            id="dropdown-diet"
            role="menu"
          >
            <div tabIndex="0" className={`dropdown-content ${styles.stopBorder}`} onBlur={e => {document.getElementById("dropdown-diet").classList.remove(styles.show)}}>
              {Object.keys(diet).map((key, idx) => (
                <DropItem
                  key={idx}
                  name={key}
                  is_checked={diet[key]}
                  add={add_category}
                  remove={remove_category}
                  category="diet_req"
                />
              ))}
            </div>
          </div>
        </div>
      </div>
      <div style={{ height: "150px" }}></div>
    </div>
  );
}

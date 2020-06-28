import styles from "./Pantry.module.scss";

import React from "react";

export default class Indicator extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      section: [
        { title: "Dairy", ingredients: ["Milk", "Cheese", "Butter", "Creme"] },
        {
          title: "Meats",
          ingredients: ["Beef Sausage", "Salami", "Smoked Salmon"],
        },
      ],
    };
  }
  render() {
    return (
      <div className={styles.pantry}>
        <h1 className="title">The pantry.</h1>
        <div className="control">
          <input className="input" placeholder="Add an item" />
        </div>
        <div className={styles.ingredientSection}>
          {this.state.section.map((section, i) => (
            <div key={i}>
              <h4>{section.title}</h4>
              <div className="tags">
                {section.ingredients.map((ingredient, j) => (
                  <span key={j} className="tag is-dark">
                    {ingredient}
                  </span>
                ))}
              </div>
            </div>
          ))}
        </div>
      </div>
    );
  }
}

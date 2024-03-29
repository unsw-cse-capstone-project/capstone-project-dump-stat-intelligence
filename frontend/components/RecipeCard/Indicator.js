import styles from "./RecipeCard.module.scss";

import React from "react";

export default class Indicator extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hover: false };
  }
  render() {
    return (
      <div
        onMouseOver={() => this.setState({ hover: true })}
        onMouseLeave={() => this.setState({ hover: false })}
        className={styles.indicator}
        style={{
          backgroundColor: this.props.value <= 3 ? "#40b983" : "#ffbd2d",
        }}
      >
        {!this.state.hover ? (
          this.props.value
        ) : (
          <div className={styles.indicator.open}>
            <h6 className={styles.needs}>{this.props.perfect ? "Ready to cook!" : "You need"}:</h6>
            {this.props.children}
          </div>
        )}
      </div>
    );
  }
}

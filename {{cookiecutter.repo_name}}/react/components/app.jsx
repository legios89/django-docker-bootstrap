/* global gettext */
var React = require('react');

var App = React.createClass({
  propTypes: {
    children: React.PropTypes.any
  },

  render: function () {
    return (
      <div className="site-wrapper-inner">
        <div className="cover-container">
          <div className="masthead clearfix">
            <div className="inner">
              <h3 className="masthead-brand">{gettext('Home')}</h3>
              <nav>
                <ul className="nav masthead-nav">
                  <li className="active"><a href="">{gettext('Home')}</a></li>
                  <li>
                    <a href="/admin/">{gettext('Admin')}</a>
                  </li>
                </ul>
              </nav>
            </div>
          </div>
          <div className="inner cover">
            {this.props.children}
          </div>
        </div>
      </div>);
  }
});
module.exports = App;

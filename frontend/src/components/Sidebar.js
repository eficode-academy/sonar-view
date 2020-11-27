import React, { useState } from "react";
import { compile } from "path-to-regexp";
import PropTypes from "prop-types";
import styled from "styled-components";
import { Link, withRouter } from "react-router-dom";
import { Flex, Box } from "rebass";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faBars, faTimes } from "@fortawesome/free-solid-svg-icons";
import NavLink from "./NavLink";
import Logo from "./Logo";



const Wrapper = styled.div`
  padding: 20px 40px;
  width: 280px;
  border-right: 1px solid ${(props) => props.theme.colors.lightGrey};
  height: 100vh;
  position: sticky;
  overflow: scroll;
  transition: left 0.3s ease-in;
  background-color: white;

  ${(props) => props.theme.media.md`
  left: -100%;
  width: 100%;
  position: absolute;

      ${
        props.isOpen &&
        `
left: 0;

      `
      }
  `}
`;

const MenuButton = styled.button`
  border: none;
  background-color: transparent;
  position: absolute;
  top: 20px;
  left: 20px;
  display: none;
  ${({ theme }) => theme.media.md`
       display: block;
  `};
`;

const CloseButton = styled.button`
  border: none;
  background-color: transparent;
  display: none;
  ${({ isOpen, theme }) => isOpen && theme.media.md && `display: block`}
`;
// TODO: Rethink the side bar structure
function Sidebar({ match, data, isLoading }) {
  const [isOpen, setIsOpen] = useState(false);

  const urlPath = Object.keys(data).join("");

  return (
    <>
      <MenuButton onClick={() => setIsOpen(true)}>
        <FontAwesomeIcon icon={faBars} as="button" />
      </MenuButton>
      
      <Wrapper isOpen={isOpen}>
        <Flex flexDirection="column">
          <Flex
            width={["100%", "100%", "120px"]}
            mb="70px"
            justifyContent="space-between"
          >
            <Link to="/">
              <Box width="120px">
                <Logo />
              </Box>
            </Link>
            <CloseButton onClick={() => setIsOpen(false)} isOpen={isOpen}>
              <FontAwesomeIcon icon={faTimes} />
            </CloseButton>
          </Flex>
          {!isLoading &&
            data[urlPath]?.map((item, i) => {
              let pathToPage = "";
              const setPath = compile(match.path);

              if (match.params.email) {
                const newPath = setPath({
                  ...match.params,
                  email: item.email,
                  date: match.params.date,
                });

                pathToPage = newPath;
              }
              if (!match.params.email && !match.params.date) {
                pathToPage = `/${urlPath}/${item[i]}`;
              } else if (match.params.date && !match.params.email) {
                pathToPage = `${match.url}/${item.email}`;
              }

              return (
                <NavLink
                  href={pathToPage}
                  title={item.name || item[i]}
                  key={item.name || item[i]}
                  onClick={() => setIsOpen(false)}
                />
              );
            })}

        </Flex>  
      </Wrapper>
    </>

  );
}

Sidebar.defaultProps = {
  isLoading: true,
};

Sidebar.propTypes = {
  isLoading: PropTypes.bool,
  data: PropTypes.objectOf(PropTypes.any).isRequired,
  match: PropTypes.shape({
    path: PropTypes.string,
    url: PropTypes.string,
    params: PropTypes.shape({
      email: PropTypes.string,
      date: PropTypes.string,
    }),
  }).isRequired,
};

export default withRouter(Sidebar);
